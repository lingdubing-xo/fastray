"""
@file: response.py
@author: lingdubing
@desc: 返回响应模型
@character: utf-8
"""

from pydantic import Field, BaseModel
from typing import Optional, List

STATUS_CODE = {
    "success": 200,
    "error": 500,
    "warning": 400,
    "info": 201,
    "unauthorized": 401,
    "forbidden": 403,
    "not_found": 404,
    "method_not_allowed": 405,
    "conflict": 409,
    "internal_server_error": 500,
    "unprocessable entity": 422,
    "unsupported media type": 415
}

class ReturnNoneDataModel(BaseModel):
    success: bool = Field(False, title="是否成功", description="是否成功")
    message: str = Field(..., title="消息", description="这是消息")
    code: Optional[int] = Field(None, ge=200, le=599, title="状态码", description="状态码")


class ReturnDataModel(ReturnNoneDataModel):
    total: int = Field(0, title="总数", description="总数")
    data: List[dict] = Field(None, title="数据", description="数据")

class ReturnTokenModel(ReturnNoneDataModel):
    token: Optional[str] = Field(None, title="登录令牌", description="token")



