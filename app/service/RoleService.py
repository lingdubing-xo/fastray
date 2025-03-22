"""
@file: RoleService.py
@author: lingdubing
@desc: 角色设施文件
@character: utf-8
"""

from ..models.models import Role
from .BaseService import BaseService
from typing import Optional

class RoleService(BaseService[Role]):
    def __init__(self):
        super().__init__(Role, id_field="role_id")

    def get_role_by_role_id(self, role_id: int) -> Optional[Role]:
        """根据角色ID获取角色"""
        return self.get_by_id(role_id)
