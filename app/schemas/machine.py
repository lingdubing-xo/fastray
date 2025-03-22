"""
@file: machine_schemas.py
@author: lingdubing
@desc: 电动车业务模型约束
@character: utf-8
"""

from pydantic import Field
from .type import PaginationBase,FormJsonBase
from typing import Optional, Dict


class MachinePaingtionModel(PaginationBase):
    page: int = Field(1, description="页码")
    page_size: int = Field(10, description="每页数量")
    status: Optional[int] = Field(None, description="状态")
    area_id: Optional[str] = Field(None, description="区域ID")
    machine_id: Optional[str] = Field(None, description="电动车ID")

class AddMachineModel(FormJsonBase):
    machine_point: Dict[str, float] = Field(..., description="电动车位置 {longitude, latitude}")

class RideMachineModel(FormJsonBase):
    machine_id: str = Field(..., description="电动车ID")
    machine_origin: Dict[str, float] = Field(..., description="起点 {longitude, latitude}")
    machine_destination: Dict[str, float] = Field(..., description="终点 {longitude, latitude}")
