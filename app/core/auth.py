"""
@file: Auth.py
@author: lingdubing
@desc: 安全验证类
@character: utf-8
"""

from typing import Optional, Tuple
from fastapi import Depends, HTTPException, Header, Request
from ..schemas.response import STATUS_CODE
import jwt
from config import settings
from ..service.UserService import UserService
from ..service.UserRoleService import UserRoleService
from ..service.AccessService import AccessService
from ..service.RoleAccessService import RoleAccessService

def _raise_auth_exception(detail: str, token: Optional[str] = None) -> None:
    """辅助函数：抛出认证相关的 HTTPException"""
    headers = {"WWW-Authenticate": f"Bearer {token}" if token else "Bearer"}
    raise HTTPException(
        status_code=STATUS_CODE["unauthorized"],
        detail=detail,
        headers=headers
    )


async def verify_token(authorization: Optional[str] = Header(None)) -> Tuple[str, str]:
    """
    验证 JWT token 并返回用户ID和角色ID

    :param authorization: HTTP Authorization 头，格式为 "Bearer <token>"
    :return: Tuple[user_id, role_id]
    :raises HTTPException: 如果 token 无效或用户无权限
    """
    if not authorization or not authorization.startswith("Bearer "):
        _raise_auth_exception("无效凭证")

    token = authorization[7:]  # 提取 "Bearer " 后的 token

    try:
        # 解密 token
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        username = payload.get("username")

        if not username:
            _raise_auth_exception("无效凭证", token)

        # 获取用户信息
        user_service = UserService()
        user_info = user_service.get_user_by_username(username)
        if not user_info or user_info.user_status == 0:
            _raise_auth_exception("无效凭证，无用户信息", token)

        # 获取用户角色
        user_role_service = UserRoleService()
        user_role = user_role_service.get_user_role_link(user_info.user_id)
        if not user_role:
            _raise_auth_exception("无效凭证，无角色分配", token)

        return user_info.user_id, user_role.role_id

    except jwt.ExpiredSignatureError:
        _raise_auth_exception("凭证已过期", token)
    except jwt.InvalidTokenError:
        _raise_auth_exception("无效凭证", token)


async def check_permission(request: Request, user_info: Tuple[str, str] = Depends(verify_token)) -> Tuple[str, str]:
    """
    检查接口权限

    :param request: HTTP 请求对象
    :param user_info: 从 verify_token 返回的 (user_id, role_id)
    :return: Tuple[user_id, role_id] 如果有权限
    :raises HTTPException: 如果无权限
    """
    user_id, role_id = user_info
    permission_name = request.url.path.split('/')[-1]  # 提取路径末尾作为权限名

    # 获取角色权限
    role_access_service = RoleAccessService()
    access_service = AccessService()
    access_list = role_access_service.get_access_by_role(role_id)
    access_scopes = [
        access_service.get_access_by_id(access.access_id).access_url
        for access in access_list
    ]

    if permission_name not in access_scopes:
        _raise_auth_exception("没有权限")

    return user_id, role_id
