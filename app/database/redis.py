"""
@file: redis.py
@author: lingdubing
@desc: redis初始化文件
@character: utf-8
"""

from functools import lru_cache
import aioredis
from aioredis import Redis
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from config import settings

class RedisPool:
    _pools = {}

    @classmethod
    @lru_cache(maxsize=128)
    def get_pool(cls, db: int) -> aioredis.ConnectionPool:
        if db not in cls._pools:
            cls._pools[db] = aioredis.ConnectionPool.from_url(
                f"redis://{settings.cache_host}:{settings.cache_port}",
                db=db,
                encoding='utf-8',
                decode_responses=True
            )
        return cls._pools[db]

@asynccontextmanager
async def redis_client(db: int) -> AsyncGenerator[Redis, None]:
    """获取 Redis 客户端的异步上下文管理器"""
    try:
        pool = RedisPool.get_pool(db)
        client = Redis(connection_pool=pool)
        yield client
    except aioredis.RedisError as e:
        raise RuntimeError(f"Failed to connect to Redis (db={db}): {str(e)}")
    finally:
        await client.close()
@asynccontextmanager
async def task_cache() -> AsyncGenerator[Redis, None]:
    """骑行任务的缓存"""
    async with redis_client(int(settings.task_cache_db)) as client:
        yield client
@asynccontextmanager
async def code_cache() -> AsyncGenerator[Redis, None]:
    """短信验证码的缓存"""
    async with redis_client(int(settings.code_cache_db)) as client:
        yield client
@asynccontextmanager
async def token_cache() -> AsyncGenerator[Redis, None]:
    """验证和刷新 token 的缓存"""
    async with redis_client(int(settings.token_cache_db)) as client:
        yield client
