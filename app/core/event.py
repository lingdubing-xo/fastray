"""
@file: event.py
@author: lingdubing
@desc: FastAPI 事件
@character: utf-8
"""

from typing import Callable
from fastapi import FastAPI
from ..database.mysql import register
from ..database.redis import RedisPool
from aioredis import Redis
from config import settings
from rich.console import Console
import asyncio
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn

console = Console()

def startup(app: FastAPI) -> Callable[[], None]:
    """
    FastAPI 启动事件
    :param app: FastAPI 实例
    :return: 启动函数
    """
    async def app_start() -> None:
        console.print("[bold green]-------------FastRay start-------------", justify="center")
        console.print("[cyan]晴空一鹤排云上, 便引诗情到碧霄", justify="center")
        console.print("[yellow]@author lingdubing", justify="center")
        console.print()

        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            TimeRemainingColumn(),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Starting FastRay...", total=100)
            progress.update(task, advance=30, description="[cyan]Registering database...")
            await register()
            progress.update(task, advance=30, description="[cyan]Initializing Redis caches...")
            app.state.token_cache = Redis(connection_pool=RedisPool.get_pool(int(settings.token_cache_db)))
            app.state.code_cache = Redis(connection_pool=RedisPool.get_pool(int(settings.code_cache_db)))
            app.state.task_cache = Redis(connection_pool=RedisPool.get_pool(int(settings.task_cache_db)))
            progress.update(task, advance=40, description="[green]Finalizing startup...")
            await asyncio.sleep(0.5)

        console.print("[bold green]FastRay started successfully!", justify="center")

    return app_start

def stopping(app: FastAPI) -> Callable[[], None]:
    """
    FastAPI 停止事件
    :param app: FastAPI 实例
    :return: 停止函数
    """
    async def stop_app() -> None:
        console.print("[bold red]-------------FastRay stop-------------", justify="center")
        console.print("[cyan]郴江幸自绕郴山，为谁流下潇湘去", justify="center")
        console.print("[yellow]@author lingdubing", justify="center")
        console.print()


        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            TimeRemainingColumn(),
            console=console
        ) as progress:
            task = progress.add_task("[red]Stopping FastRay...", total=100)

            # 关闭 Redis 客户端
            redis_clients = [
                app.state.task_cache,
                app.state.code_cache,
                app.state.token_cache
            ]

            progress.update(task, advance=30, description="[red]Closing Redis caches...")
            for client in redis_clients:
                if isinstance(client, Redis) and client.connection_pool:
                    await client.close()
                    await client.connection_pool.disconnect()


            progress.update(task, advance=60, description="[red]Finalizing shutdown...")

        console.print("[bold red]FastRay stopped successfully!", justify="center")

    return stop_app
