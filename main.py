"""
@file: main.py
@author: lingdubing
@time: 2024/10/31  14:11
@desc: 程序的入口
@character: utf-8
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from config import settings
from app.core import event, router, exception
from app.core.log_midderware import LogRequestMiddleware


application = FastAPI(
    debug=settings.app_debug,
)

# 静态文件挂载
application.mount("/resources/static", StaticFiles(directory=settings.static_dir))

# 事件监听
application.add_event_handler("startup", event.startup(application))
application.add_event_handler("shutdown", event.stopping(application))

# 日志中间价
application.add_middleware(LogRequestMiddleware)

# 异常处理
exception.register_exception_handlers(application)

# 路由挂载
application.include_router(router.router)

app = application

