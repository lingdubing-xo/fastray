"""
@file: record_schemas.py
@author: lingdubing
@desc: 订单业务模型约束
@character: utf-8
"""

from pydantic import Field
from .type import PaginationBase
from typing import Optional


class RecordPaingtionModel(PaginationBase):
    page: int = Field(1, description="页码")
    page_size: int = Field(10, description="每页数量")
    time_range: Optional[str] = Field(None, description="时间范围")
    record_id: Optional[str] = Field(None, description="订单号")
