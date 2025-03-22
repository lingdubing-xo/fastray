"""
@file: UserService.py
@author: lingdubing
@desc: 用户设施文件
@character: utf-8
"""

from ..models.models import User
from .BaseService import BaseService
from sqlmodel import select
from typing import Optional, Tuple, List
from ..utils.crypto_utils import en_password, generate_uuid

class UserService(BaseService[User]):
    def __init__(self):
        super().__init__(User, id_field="user_id")

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        """根据用户ID获取用户"""
        return self.get_by_id(user_id)

    def get_user_by_username(self, username: str) -> Optional[User]:
        """根据用户名获取用户"""
        with self.get_session() as session:
            statement = select(User).where(User.username == username)
            return session.exec(statement).first()

    def create_user(self, username: str, password: str) -> User:
        """创建新用户"""
        user_id = generate_uuid()
        hashed_password = en_password(password)
        new_user = User(
            user_id=user_id,
            username=username,
            password=hashed_password,
            user_status=1,
            create_by=user_id,
            update_by=user_id
        )
        return self.create(new_user)

    def update_password_by_username(self, username: str, new_password: str) -> bool:
        """根据用户名更新密码"""
        user = self.get_user_by_username(username)
        if user:
            user.password = en_password(new_password)
            self.update(user)
            return True
        return False

    def update_user_status(self, user_id: str) -> bool:
        """切换用户状态（0 -> 1 或 1 -> 0）"""
        user = self.get_user_by_id(user_id)
        if user:
            user.user_status = 1 if user.user_status == 0 else 0
            self.update(user)
            return True
        return False

    def get_user_list(self, page: int, page_size: int, user_status: Optional[int] = None,
                      user_id: Optional[str] = None) -> Tuple[List[User], int]:
        """获取用户列表（分页）"""
        filters = []
        if user_status is not None:
            filters.append(User.user_status == user_status)
        if user_id is not None:
            filters.append(User.user_id == user_id)
        return self.get_paginated(page, page_size, filters=filters)
