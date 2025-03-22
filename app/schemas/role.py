"""
@file: role_schemas.py
@author: lingdubing
@desc: 角色业务模型约束
@character: utf-8
"""

from pydantic import Field
from .type import PaginationBase

class RolePaingtionModel(PaginationBase):
    page: int = Field(1, description="页码")
    page_size: int = Field(10, description="每页数量")
