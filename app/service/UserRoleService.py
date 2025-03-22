"""
@file: UserRoleService.py
@author: lingdubing
@desc: 用户角色设施文件
@character: utf-8
"""

from ..models.models import UserRoleLink
from .BaseService import BaseService
from sqlmodel import select
from typing import Optional, List, Dict, Union

class UserRoleService(BaseService[UserRoleLink]):
    """用户角色关联服务类"""

    def __init__(self):
        super().__init__(UserRoleLink, id_field=None)

    def get_by_composite_id(self, user_id: str, role_id: str) -> Optional[UserRoleLink]:
        """根据复合主键获取用户角色关联"""
        id_value = {"user_id": user_id, "role_id": role_id}
        return self.get_by_id(id_value)

    def assign_role_to_user(self, user_id: str, role_id: str) -> UserRoleLink:
        """为用户分配角色"""
        new_user_role = UserRoleLink(
            user_id=user_id,
            role_id=role_id,
            create_by=user_id,
            update_by=user_id
        )
        return self.create(new_user_role)

    def get_users_by_role(self, role_id: Optional[str] = None) -> List[UserRoleLink]:
        """获取具有特定角色的所有用户关联"""
        with self.get_session() as session:
            statement = select(UserRoleLink)
            if role_id is not None:
                statement = statement.where(UserRoleLink.role_id == role_id)
            result = session.exec(statement)
            return result.all()

    def get_user_role_link(self, user_id: Optional[str] = None) -> Optional[UserRoleLink]:
        """获取特定用户的角色关联（仅基于user_id）"""
        with self.get_session() as session:
            statement = select(UserRoleLink)
            if user_id is not None:
                statement = statement.where(UserRoleLink.user_id == user_id)
            result = session.exec(statement)
            return result.first()

    def update_user_role_link(self, user_id: str, new_role_id: str) -> Optional[UserRoleLink]:
        """更新用户的角色关联（仅需 user_id 和新的 role_id）"""
        user_role_link = self.get_user_role_link(user_id)
        if user_role_link:
            user_role_link.role_id = new_role_id
            user_role_link.update_by = user_id
            return self.update(user_role_link)
        return None
