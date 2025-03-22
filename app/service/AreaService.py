"""
@file: AreaService.py
@author: lingdubing
@desc: 区域设施文件
@character: utf-8
"""

from ..models.models import Area
from .BaseService import BaseService
from sqlmodel import select
from typing import Optional, List

class AreaService(BaseService[Area]):
    """区域服务类"""

    def __init__(self):
        """
        初始化区域服务
        """
        super().__init__(Area, id_field="area_id")

    def get_area_by_id(self, area_id: int) -> Optional[Area]:
        """根据区域ID获取区域"""
        with self.get_session() as session:
            statement = select(Area).where(Area.area_id == area_id)
            return session.exec(statement).first()

    def get_all_area(self) -> List[Area]:
        """获取所有非根区域（area_id != 0）"""
        with self.get_session() as session:
            statement = select(Area).where(Area.area_id != 0)
            return session.exec(statement).all()
