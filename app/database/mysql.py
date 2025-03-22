"""
@file: mysql.py
@author: lingdubing
@desc: mysql初始化文件
@character: utf-8
"""

from sqlmodel import SQLModel, create_engine
from config import settings
from ..models.models import User, Machine, Role, Access, Area, Record, UserRoleLink, RoleAccessLink



engine = create_engine(f"mysql+pymysql://{settings.mysql_user}:{settings.mysql_password}@{settings.mysql_ip}:{settings.mysql_port}/{settings.mysql_database}")


async def register():
    SQLModel.metadata.create_all(engine)
