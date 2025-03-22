"""
@file: user_schemas.py
@author: lingdubing
@desc: 用户业务模型约束
@character: utf-8
"""

from pydantic import Field
from fastapi import Form
from .type import FormJsonBase, PaginationBase, PhoneNumber
from typing import Optional

class RegisterModel(FormJsonBase):
    """用户注册模型"""
    username: PhoneNumber
    password: str = Field(..., description="密码")
    ver_code: str = Field(..., description="验证码")

class LoginModel(FormJsonBase):
    """用户登录模型"""
    username: PhoneNumber
    password: Optional[str] = Field(None, description="密码")
    ver_code: Optional[str] = Field(None, description="验证码")

class UpdatePasswordModel(FormJsonBase):
    """更新密码模型"""
    username: PhoneNumber
    password: Optional[str] = Field(None, description="密码")
    ver_code: Optional[str] = Field(None, description="验证码")


class UserPaginationModel(PaginationBase):
    """用户分页模型"""
    user_id: str | None = Field(None, description="用户编号")
    user_role_id: int | None = Field(None, description="用户角色编号")
    user_status: int | None = Field(None, description="用户状态")
