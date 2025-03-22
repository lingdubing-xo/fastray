"""
@file: user.py
@author: lingdubing
@desc: 操作用户行为的接口层
@character: utf-8
"""

from fastapi import APIRouter, Depends
from ...schemas.response import ReturnNoneDataModel, ReturnDataModel, ReturnTokenModel, STATUS_CODE
from ...service.UserService import UserService
from ...service.UserRoleService import UserRoleService
from ...service.RoleService import RoleService
from ...schemas.type import PhoneNumber, get_model, Uuid
from ...schemas.user import RegisterModel, LoginModel, UpdatePasswordModel, UserPaginationModel
from ...utils.sms_utils import send_code, generate_code
from ...utils.crypto_utils import generate_token, check_password
from ...database.redis import code_cache
from ...core.auth import check_permission
from config import settings


router = APIRouter()

@router.get("/check",summary="用户存在检查", response_model=ReturnNoneDataModel)
async def check_user(username: PhoneNumber):
    """
    检查用户是否存在
    :param username:
    :return:
    """

    user_service = UserService()
    user = user_service.get_user_by_username(username)

    if user:
        return ReturnNoneDataModel(code=200, message="查询成功，用户已注册", success=True)
    return ReturnNoneDataModel(code=200, message="查询成功，用户未注册", success=False)


@router.get("/getcode", summary="用户获取验证码", response_model=ReturnNoneDataModel)
async def get_code(username: PhoneNumber):
    """
    获取验证码
    :param username: 用户名
    :return: 验证码发送结果
    """
    async with code_cache() as code_cache_instance:
        code = generate_code()
        pipeline = code_cache_instance.pipeline()
        pipeline.set(username, code, ex=90)  # 设置验证码过期时间为90秒
        await pipeline.execute()

        # 发送短信验证码
        result = send_code(username, code)
        if str(result) == "0":
            return ReturnNoneDataModel(
                code=STATUS_CODE["success"],
                message="验证码发送成功",
                success=True
            )
        else:
            exp = settings.msg_status_codes.get(str(result), "未知错误")
            return ReturnNoneDataModel(
                code=STATUS_CODE["error"],
                message=f"验证码发送失败: {exp}",
                success=False
            )


@router.post('/register', summary="用户注册", response_model=ReturnNoneDataModel)
async def register(user: RegisterModel = Depends(get_model(RegisterModel))):
    """
    用户注册
    :param user: 注册模型，包含用户名、密码和验证码
    :return: 注册结果
    """
    # 使用上下文管理器操作Redis验证码缓存
    async with code_cache() as cache:
        # 检查验证码是否存在
        if not await cache.exists(user.username):
            return ReturnNoneDataModel(
                code=STATUS_CODE["warning"],
                message="验证码已过期",
                success=False
            )

        # 验证验证码
        redis_code = await cache.get(user.username)
        if redis_code != user.ver_code:
            return ReturnNoneDataModel(
                code=STATUS_CODE["error"],
                message="验证码错误",
                success=False
            )

        # 验证通过后删除验证码
        await cache.delete(user.username)

    # 用户服务操作
    user_service = UserService()
    # 检查用户名是否已存在
    if user_service.get_user_by_username(user.username):
        return ReturnNoneDataModel(
            code=STATUS_CODE["warning"],
            message="该账号已注册过",
            success=True
        )

    # 创建新用户
    new_user = user_service.create_user(user.username, user.password)

    # 分配默认角色
    user_role_service = UserRoleService()
    default_role_id = settings.role_dict["user"]
    user_role_service.assign_role_to_user(new_user.user_id, default_role_id)

    return ReturnNoneDataModel(
        code=STATUS_CODE["success"],
        message="注册成功",
        success=True
    )

@router.post('/login', summary="用户登录", response_model=ReturnTokenModel)
async def login(user: LoginModel = Depends(get_model(LoginModel))):
    """
    用户登录

    :param user: 登录模型，包含用户名、密码和验证码（可选）
    :return: 登录结果和token
    """

    # 创建 UserService 实例
    user_service = UserService()

    # 查询用户信息
    user_info = user_service.get_user_by_username(user.username)
    if not user_info or user_info.user_status == 0:
        return ReturnTokenModel(
            code=STATUS_CODE["error"],
            message="账号不存在或已被禁用",
            success=False,
            token=None
        )

    # 根据输入验证方式处理
    if user.ver_code:  # 验证码登录
        async with code_cache() as cache:
            if not await cache.exists(user.username):
                return ReturnTokenModel(
                    code=STATUS_CODE["warning"],
                    message="验证码已过期",
                    success=False,
                    token=None
                )
            redis_code = await cache.get(user.username)
            if redis_code != user.ver_code:
                return ReturnTokenModel(
                    code=STATUS_CODE["error"],
                    message="验证码错误",
                    success=False,
                    token=None
                )
            token = generate_token(user.username)
            await cache.delete(user.username)
            return ReturnTokenModel(
                code=STATUS_CODE["success"],
                message="登录成功",
                success=True,
                token=token
            )

    elif user.password:  # 密码登录
        if check_password(user.password, user_info.password):
            token = generate_token(user.username)
            return ReturnTokenModel(
                code=STATUS_CODE["success"],
                message="登录成功",
                success=True,
                token=token
            )
        return ReturnTokenModel(
            code=STATUS_CODE["error"],
            message="密码错误",
            success=False,
            token=None
        )

    return ReturnTokenModel(
        code=STATUS_CODE["error"],
        message="请提供密码或验证码",
        success=False,
        token=None
    )

@router.post("/updatepsw", summary="更改用户密码", response_model=ReturnNoneDataModel)
async def update_usr(user: UpdatePasswordModel = Depends(get_model(UpdatePasswordModel))):
    """
    更改用户密码
    :return:
    """
    async with code_cache() as cache:
        # 检查验证码是否存在
        if not await cache.exists(user.username):
            return ReturnNoneDataModel(
                code=STATUS_CODE["warning"],
                message="验证码已过期",
                success=False
            )

        # 验证验证码
        redis_code = await cache.get(user.username)
        if redis_code != user.ver_code:
            return ReturnNoneDataModel(
                code=STATUS_CODE["error"],
                message="验证码错误",
                success=False
            )

        # 验证通过后删除验证码
        await cache.delete(user.username)

    # 创建 UserService 实例
    user_service = UserService()

    # 调用 UserService 更新密码
    password_updated = user_service.update_password_by_username(user.username, user.password)

    if password_updated:
        return ReturnNoneDataModel(code=STATUS_CODE["success"], message="更改密码成功", success=True)
    else:
        return ReturnNoneDataModel(code=STATUS_CODE["error"], message="该用户不存在", success=False)


@router.get("/update_user_status", summary="更改用户状态", response_model=ReturnNoneDataModel,
            dependencies=[Depends(check_permission)])
async def update_user_status(user_id: Uuid):
    """
    更改用户启用禁用状态

    :param user_id: 用户ID
    :return: 更新结果
    """
    # 创建 UserService 实例
    user_service = UserService()

    # 调用 UserService 更新用户状态
    user_updated = user_service.update_user_status(user_id)

    if user_updated:
        return ReturnNoneDataModel(code=STATUS_CODE["success"], message="更改用户状态成功", success=True)
    else:
        return ReturnNoneDataModel(code=STATUS_CODE["error"], message="该用户不存在", success=False)


@router.get("/update_user_role", summary="更改用户角色", response_model=ReturnNoneDataModel,
            dependencies=[Depends(check_permission)])
async def update_user_role(user_id: Uuid, role_id: str):
    """
    更改用户角色

    :param user_id: 用户ID
    :param role_id: 角色ID
    :return: 更新结果
    """
    # 创建 UserRoleService 实例
    user_role_service = UserRoleService()

    # 调用 UserRoleService 更新用户角色
    user_updated = user_role_service.update_user_role_link(user_id, role_id)

    if user_updated:
        return ReturnNoneDataModel(code=STATUS_CODE["success"], message="更改用户角色成功", success=True)
    else:
        return ReturnNoneDataModel(code=STATUS_CODE["error"], message="该用户不存在", success=False)


@router.post("/userlist", summary="获取用户列表", response_model=ReturnDataModel,
             dependencies=[Depends(check_permission)])
async def get_user_list(query: UserPaginationModel = Depends(get_model(UserPaginationModel))):
    """
    获取用户列表，并根据状态和角色筛选，分页基于所有用户总数

    :param query: 分页查询参数，包括 page, page_size, user_status, user_id, user_role_id
    :return: 用户列表和所有用户总数
    """
    # 创建服务实例
    user_service = UserService()
    user_role_service = UserRoleService()
    role_service = RoleService()

    # 获取过滤后的用户列表和所有用户总数
    user_list, total = user_service.get_user_list(
        page=query.page,
        page_size=query.page_size,
        user_status=query.user_status,
        user_id=query.user_id
    )

    if total <= 0:
        # 如果总数为0，表示无用户数据
        return ReturnDataModel(
            code=STATUS_CODE["error"],
            message="查询用户列表错误，无用户数据",
            success=False,
            data=[],
            total=0
        )

    if not user_list:
        # 如果当前页无数据但总数大于0，返回空列表（分页超出范围）
        return ReturnDataModel(
            code=STATUS_CODE["success"],
            message="获取用户列表成功",
            success=True,
            data=[],
            total=total
        )

    # 如果指定了角色 ID，进一步过滤用户列表
    if query.user_role_id:
        role_filtered_users = user_role_service.get_users_by_role(role_id=query.user_role_id)
        role_filtered_user_ids = {user_role.user_id for user_role in role_filtered_users}
        user_list = [user for user in user_list if user.user_id in role_filtered_user_ids]

    # 构建最终用户列表，包含角色名称
    final_user_list = [
        {
            "create_time": user.create_time,
            "user_id": user.user_id,
            "username": user.username,
            "user_status": user.user_status,
            "role_name": (role.role_name if (
                        role_link and (role := role_service.get_role_by_role_id(role_link.role_id))) else None)
        }
        for user in user_list
        if (role_link := user_role_service.get_user_role_link(user_id=user.user_id)) or True  # 即使无角色也包含用户
    ]

    return ReturnDataModel(
        code=STATUS_CODE["success"],
        message="获取用户列表成功",
        success=True,
        data=final_user_list,
        total=total  # 返回所有用户总数
    )





