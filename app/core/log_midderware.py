"""
@file: log_midderware.py
@author: lingdubing
@desc: 请求日志中间件
@character: utf-8
"""

import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import datetime
from config import settings

# 配置日志
logger = logging.getLogger(__name__)
log_file = settings.log_dir / f"api-{datetime.date.today().isoformat()}.log"

# 确保日志目录存在
settings.log_dir.mkdir(exist_ok=True)

# 设置日志处理器
handler = logging.FileHandler(log_file)
handler.setFormatter(logging.Formatter(settings.log_format, datefmt=settings.log_datefmt))
logger.addHandler(handler)
logger.setLevel(getattr(logging, settings.log_level.upper(), logging.INFO))

class LogRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        """记录请求日志"""
        try:
            add_time = datetime.datetime.now().strftime(settings.log_datefmt)
            basic_info = (
                f"time={add_time}, method={request.method}, url={request.url}, "
                f"client_ip={request.client.host}"
            )

            if request.method in ["POST", "PUT"]:
                body = await request.body()
                log_message = f"{basic_info}, body={body.decode('utf-8', errors='ignore')}"
            else:
                log_message = basic_info

            logger.info(log_message)
        except Exception as e:
            logger.error(f"Failed to log request: {str(e)}")

        response = await call_next(request)
        return response
