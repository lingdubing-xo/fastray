"""
@file: RoleAccessService.py
@author: lingdubing
@desc: 角色权限设施文件
@character: utf-8
"""

from ..models.models import RoleAccessLink
from .BaseService import BaseService
from sqlmodel import select
from typing import Optional, List

class RoleAccessService(BaseService[RoleAccessLink]):
    """角色权限关联服务类"""

    def __init__(self):
        """
        初始化角色权限服务
        """
        super().__init__(RoleAccessLink, id_field=None)

    def get_by_composite_id(self, role_id: str, access_id: str) -> Optional[RoleAccessLink]:
        """根据复合主键获取角色权限关联"""
        id_value = {"role_id": role_id, "access_id": access_id}
        return self.get_by_id(id_value)

    def get_access_by_role(self, role_id: str) -> List[RoleAccessLink]:
        """获取指定角色的所有权限关联"""
        with self.get_session() as session:
            statement = select(RoleAccessLink).where(RoleAccessLink.role_id == role_id)
            return session.exec(statement).all()

    def create_role_access(self, user_id: str, access_id: str, role_id: str) -> RoleAccessLink:
        """创建角色权限关联，如果已存在则跳过"""
        existing = self.get_by_composite_id(role_id, access_id)
        if existing:
            return existing  # 如果已存在，直接返回现有记录
        role_access_link = RoleAccessLink(
            role_id=role_id,
            access_id=access_id,
            create_by=user_id,
            update_by=user_id
        )
        return self.create(role_access_link)

    def delete_role_access(self, role_id: str, access_id: str) -> bool:
        """删除指定角色权限关联"""
        existing = self.get_by_composite_id(role_id, access_id)
        if existing:
            self.delete(existing)
            return True
        return False
