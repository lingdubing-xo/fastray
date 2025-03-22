"""
@file: AccessService.py
@author: lingdubing
@desc: 权限服务文件
@character: utf-8
"""

from ..models.models import Access
from .BaseService import BaseService
from sqlmodel import select
from typing import Optional, List

class AccessService(BaseService[Access]):
    """权限服务类"""

    def __init__(self):
        """
        初始化权限服务
        """
        super().__init__(Access, id_field="access_id")

    def get_access_by_id(self, access_id: str) -> Optional[Access]:
        """根据权限ID获取权限"""
        with self.get_session() as session:
            statement = select(Access).where(Access.access_id == access_id)
            return session.exec(statement).first()

    def get_access_by_id_menu(self, access_id: str) -> Optional[Access]:
        """根据权限ID获取菜单权限"""
        with self.get_session() as session:
            statement = select(Access).where(Access.access_id == access_id, Access.is_menu == True)
            return session.exec(statement).first()

    def get_verify_access(self) -> List[Access]:
        """获取需要验证的菜单权限"""
        with self.get_session() as session:
            statement = select(Access).where(Access.is_verify == True, Access.is_menu == True)
            return session.exec(statement).all()

    def get_parent_access(self, access_id: str) -> List[Access]:
        """获取指定父ID的所有子权限"""
        with self.get_session() as session:
            statement = select(Access).where(Access.parent_id == access_id)
            return session.exec(statement).all()
