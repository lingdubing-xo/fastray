"""
@file: access.py
@author: lingdubing
@desc: 操作权限行为的接口层
@character: utf-8
"""

from typing import Tuple
from fastapi import APIRouter, Depends
from ...schemas.response import ReturnDataModel, ReturnNoneDataModel, STATUS_CODE
from ...service.AccessService import AccessService
from ...service.RoleAccessService import RoleAccessService
from ...core.auth import verify_token, check_permission

router = APIRouter()


@router.get('/load_access', summary="动态加载权限菜单", response_model=ReturnDataModel)
async def load_access(user_info: Tuple[str, str] = Depends(verify_token)):
    """
    动态加载菜单权限

    :param user_info: 用户信息 (user_id, role_id) 从 verify_token 获取
    :return: 菜单权限列表和总数
    """
    _, role_id = user_info
    role_access_service = RoleAccessService()
    access_service = AccessService()

    # 获取角色关联的权限
    access_links = role_access_service.get_access_by_role(role_id)
    if not access_links:
        return ReturnDataModel(
            success=True,
            message="加载菜单成功，无权限数据",
            code=STATUS_CODE["success"],
            total=0,
            data=[]
        )

    # 构建菜单权限列表
    menu_access_list = [
        {
            "access_id": access.access_id,
            "access_name": access.access_name,
            "access_url": access.access_url
        }
        for link in access_links
        if (access := access_service.get_access_by_id(link.access_id)) and access.is_menu
    ]

    return ReturnDataModel(
        success=True,
        message="加载菜单成功",
        code=STATUS_CODE["success"],
        total=len(menu_access_list),
        data=menu_access_list
    )


@router.get('/verify_menu_permission', summary="验证菜单权限", response_model=ReturnNoneDataModel)
async def verify_menu_permission(path: str, user_info: Tuple[str, str] = Depends(verify_token)):
    """
    验证菜单权限

    :param path: 请求路径
    :param user_info: 用户信息 (user_id, role_id) 从 verify_token 获取
    :return: 是否有权限
    """
    _, role_id = user_info
    role_access_service = RoleAccessService()
    access_service = AccessService()

    # 获取角色关联的菜单权限 URL
    access_links = role_access_service.get_access_by_role(role_id)
    access_urls = {
        access.access_url
        for link in access_links
        if (access := access_service.get_access_by_id_menu(link.access_id)) is not None
    }

    if path not in access_urls:
        return ReturnNoneDataModel(
            code=STATUS_CODE["unauthorized"],
            message="无权限访问",
            success=False
        )
    return ReturnNoneDataModel(
        code=STATUS_CODE["success"],
        message="允许访问",
        success=True
    )


@router.get('/update_role_access', summary="增加角色权限", response_model=ReturnNoneDataModel,
            dependencies=[Depends(check_permission)])
async def update_role_access(role_id: str, access_id: str, user_info: Tuple[str, str] = Depends(check_permission)):
    """
    增加角色权限

    :param role_id: 角色ID
    :param access_id: 权限ID
    :param user_info: 用户信息 (user_id, role_id) 从 check_permission 获取
    :return: 更新结果
    """
    user_id, _ = user_info
    access_service = AccessService()
    role_access_service = RoleAccessService()

    # 创建当前权限关联
    role_access_service.create_role_access(role_id=role_id, access_id=access_id, user_id=user_id)

    # 创建父级权限关联
    parent_accesses = access_service.get_parent_access(access_id)
    for access in parent_accesses:
        role_access_service.create_role_access(role_id=role_id, access_id=access.access_id, user_id=user_id)

    return ReturnNoneDataModel(
        success=True,
        message="更新角色权限成功",
        code=STATUS_CODE["success"]
    )
