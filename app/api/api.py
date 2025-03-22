"""
@file: api.py
@author: lingdubing
@desc: 接口聚合层
@character: utf-8
"""

from .endpoints import user, role, record, access, area, machine
from .views import index
from fastapi import  APIRouter

api_router = APIRouter(prefix="/fsray")

api_router.include_router(user.router, tags=["用户行为类接口"])
api_router.include_router(role.router, tags=["角色行为类接口"])
api_router.include_router(record.router, tags=["订单行为类接口"])
api_router.include_router(access.router, tags=["权限行为类接口"])
api_router.include_router(area.router, tags=["区域行为类接口"])
api_router.include_router(machine.router, tags=["电动车行为类接口"])
api_router.include_router(index.router, tags=["首页"])

