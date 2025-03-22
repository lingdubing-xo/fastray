"""
@file: router.py
@author: lingdubing
@desc: 全局路由聚合
@character: utf-8
"""

from ..api.api import api_router
from fastapi import APIRouter


router = APIRouter()
# API路由
router.include_router(api_router)
