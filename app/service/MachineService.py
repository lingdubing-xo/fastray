"""
@file: MachineService.py
@author: lingdubing
@desc: 机器设施文件
@character: utf-8
"""

from ..models.models import Machine
from .BaseService import BaseService
from typing import Optional, Tuple, List, Dict
from ..utils.crypto_utils import generate_uuid

class MachineService(BaseService[Machine]):
    def __init__(self):
        super().__init__(Machine, id_field="machine_id")

    def get_machine_by_id(self, machine_id: str) -> Optional[Machine]:
        """根据机器ID获取机器"""
        return self.get_by_id(machine_id)

    def create_machine(self, machine_point: Dict, area_id: str, user_id: str) -> Machine:
        """创建新机器"""
        machine_id = generate_uuid()
        new_machine = Machine(
            machine_id=machine_id,
            machine_point=machine_point,
            machine_battery=100,
            area_id=area_id,
            status=1,
            create_by=user_id,
            update_by=user_id
        )
        return self.create(new_machine)

    def get_machine_list(self, page: int, page_size: int, status: Optional[int] = None,
                         machine_id: Optional[str] = None, area_id: Optional[str] = None) -> Tuple[List[Machine], int]:
        """获取机器列表（分页）"""
        filters = []
        if status is not None:
            filters.append(Machine.status == status)
        if machine_id is not None:
            filters.append(Machine.machine_id == machine_id)
        if area_id is not None:
            filters.append(Machine.area_id == area_id)
        return self.get_paginated(page, page_size, filters=filters)
