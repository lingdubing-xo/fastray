"""
@file: exception.py
@author: lingdubing
@desc: 全局异常处理
@character: utf-8
"""

import logging
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Union
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from tortoise.exceptions import DoesNotExist, IntegrityError, OperationalError, ValidationError as MysqlValidationError
from ..schemas.response import STATUS_CODE
from fastapi import FastAPI

logger = logging.getLogger(__name__)

async def handle_database_exception(request: Request, exc: Exception, message: str, status_code: int) -> JSONResponse:
    """
    通用的数据库异常处理函数
    :param request: FastAPI 请求对象
    :param exc: 异常实例
    :param message: 错误消息
    :param status_code: 状态码
    :return: JSON 响应
    """
    logger.error(f"Database error at {request.url}: {str(exc)}")
    return JSONResponse({
        "code": status_code,
        "message": message,
        "success": False
    })

async def mysql_validation_error(_: Request, exc: MysqlValidationError) -> JSONResponse:
    """数据库字段验证错误"""
    return await handle_database_exception(_, exc, str(exc), STATUS_CODE["unprocessable entity"])

async def mysql_integrity_error(_: Request, exc: IntegrityError) -> JSONResponse:
    """完整性错误"""
    message = "数据完整性错误，可能存在重复记录或违反约束"
    if "duplicate" in str(exc).lower():
        message = "记录已存在，请勿重复提交"
    return await handle_database_exception(_, exc, message, STATUS_CODE["conflict"])

async def mysql_does_not_exist(_: Request, exc: DoesNotExist) -> JSONResponse:
    """数据库记录不存在错误"""
    return await handle_database_exception(_, exc, "发出的请求针对的是不存在的记录，服务器没有进行对应的操作", STATUS_CODE["not_found"])

async def mysql_operational_error(_: Request, exc: OperationalError) -> JSONResponse:
    """数据库操作异常"""
    return await handle_database_exception(_, exc, "数据库操作失败", STATUS_CODE["internal_server_error"])

async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    """HTTP 异常处理"""
    if exc.status_code == 401:
        return JSONResponse({
            "code": STATUS_CODE["unauthorized"],
            "message": exc.detail,
            "success": False
        })
    return JSONResponse({
        "code": exc.status_code,  # 使用原始 HTTP 状态码
        "message": exc.detail,
        "success": False
    })

async def http422_error_handler(_: Request, exc: Union[RequestValidationError, ValidationError]) -> JSONResponse:
    """HTTP 422 验证错误处理"""
    logger.warning(f"Validation error: {exc.errors()}")
    return JSONResponse({
        "code": STATUS_CODE["unprocessable entity"],
        "message": f"数据校验错误: {exc.errors()}",
        "success": False
    })

def register_exception_handlers(app: FastAPI):
    """注册所有异常处理器到 FastAPI 应用"""
    app.add_exception_handler(MysqlValidationError, mysql_validation_error)
    app.add_exception_handler(IntegrityError, mysql_integrity_error)
    app.add_exception_handler(DoesNotExist, mysql_does_not_exist)
    app.add_exception_handler(OperationalError, mysql_operational_error)
    app.add_exception_handler(HTTPException, http_error_handler)
    app.add_exception_handler(RequestValidationError, http422_error_handler)
    app.add_exception_handler(ValidationError, http422_error_handler)
