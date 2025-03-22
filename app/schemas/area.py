"""
@file: area_schemas.py
@author: lingdubing
@desc: 地区业务模型约束
@character: utf-8
"""

from pydantic import Field
from .type import PaginationBase


class AreaPaingtionModel(PaginationBase):
    page: int = Field(1, description="页码")
    page_size: int = Field(10, description="每页数量")
