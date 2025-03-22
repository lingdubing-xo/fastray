"""
@file: role.py
@author: lingdubing
@desc: 操作角色行为的接口层
@character: utf-8
"""

from fastapi import APIRouter, Depends
from ...schemas.response import ReturnDataModel, STATUS_CODE
from ...schemas.type import get_model
from ...schemas.role import RolePaingtionModel
from ...service.RoleService import RoleService
from ...service.AccessService import AccessService
from ...service.RoleAccessService import RoleAccessService

router = APIRouter()

@router.post("/get_role_list", summary="获取角色列表", response_model=ReturnDataModel)
async def get_role_list(query: RolePaingtionModel = Depends(get_model(RolePaingtionModel))):
    """
    获取角色列表

    :param query: 分页查询参数，包括 page 和 page_size
    :return: 角色列表和总数
    """
    # 创建 RoleService 实例
    role_service = RoleService()

    # 获取角色列表和总数
    role_list, total = role_service.get_paginated(page=query.page, page_size=query.page_size)

    if total <= 0:
        return ReturnDataModel(
            code=STATUS_CODE["error"],
            message="查询失败，无角色数据",
            success=False,
            data=[],
            total=0
        )

    # 构建最终角色列表
    final_list = [
        {
            "create_time": role.create_time,
            "role_id": role.role_id,
            "role_name": role.role_name,
            "role_desc": role.role_desc,
        }
        for role in role_list
    ]

    return ReturnDataModel(
        code=STATUS_CODE["success"],
        message="查询成功",
        success=True,
        data=final_list,
        total=total
    )


@router.get('/get_role_menu_access', summary="获得角色需要验证的菜单权限", response_model=ReturnDataModel)
async def get_role_menu_access(role_id: str):
    """
    获取角色需要验证的菜单权限

    :param role_id: 角色ID
    :return: 菜单权限列表和总数
    """
    # 创建服务实例
    role_service = RoleService()
    access_service = AccessService()
    role_access_service = RoleAccessService()

    # 检查角色是否存在
    role_info = role_service.get_role_by_role_id(role_id)
    if not role_info:
        return ReturnDataModel(
            code=STATUS_CODE["error"],
            message="查询失败，角色ID不存在",
            success=False,
            data=[],
            total=0
        )

    # 获取需要验证的菜单权限
    verify_menu_access = access_service.get_verify_access()
    if not verify_menu_access:
        return ReturnDataModel(
            code=STATUS_CODE["success"],
            message="查询成功，无需验证的菜单权限",
            success=True,
            data=[],
            total=0
        )

    # 获取角色关联的权限ID集合
    role_access_link = role_access_service.get_access_by_role(role_id)
    role_access_ids = {link.access_id for link in role_access_link}

    # 构建最终权限列表
    verify_menu_access_list = [
        {
            "access_id": access.access_id,
            "access_name": access.access_name,
            "use": access.access_id in role_access_ids
        }
        for access in verify_menu_access
    ]

    return ReturnDataModel(
        code=STATUS_CODE["success"],
        message="查询成功",
        success=True,
        data=verify_menu_access_list,
        total=len(verify_menu_access_list)
    )
