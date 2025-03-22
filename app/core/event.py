"""
@file: event.py
@author: lingdubing
@desc: FastAPI 事件
@character: utf-8
"""

from typing import Callable
from fastapi import FastAPI
from ..database.mysql import register
from ..database.redis import RedisPool, task_cache, token_cache, code_cache
from aioredis import Redis
from config import settings


def startup(app: FastAPI) -> Callable[[], None]:
    """
    FastAPI 启动事件
    :param app: FastAPI 实例
    :return: 启动函数
    """

    async def app_start() -> None:
        print("-------------fastray start-------------")
        print("晴空一鹤排云上,便引诗情到碧霄")
        print("@author lingdubing")
        # 数据库注册
        await register()

        # 初始化 Redis 客户端并存储到 app.state
        app.state.token_cache = Redis(connection_pool=RedisPool.get_pool(int(settings.token_cache_db)))
        app.state.code_cache = Redis(connection_pool=RedisPool.get_pool(int(settings.code_cache_db)))
        app.state.task_cache = Redis(connection_pool=RedisPool.get_pool(int(settings.task_cache_db)))

    return app_start


def stopping(app: FastAPI) -> Callable[[], None]:
    """
    FastAPI 停止事件
    :param app: FastAPI 实例
    :return: 停止函数
    """

    async def stop_app() -> None:
        # 从 app.state 获取 Redis 客户端并关闭
        redis_clients = [
            app.state.task_cache,
            app.state.code_cache,
            app.state.token_cache
        ]

        for client in redis_clients:
            if isinstance(client, Redis) and client.connection_pool:
                await client.close()
                await client.connection_pool.disconnect()

        print("-------------fastray stop-------------")
        print("郴江幸自绕郴山，为谁流下潇湘去")
        print("@author lingdubing")

    return stop_app
