"""
@file: machine.py
@author: lingdubing
@desc: 操作电动车行为的接口层
@character: utf-8
"""

import ast
from typing import Tuple
from fastapi import APIRouter, Depends
from ...schemas.response import ReturnDataModel, ReturnNoneDataModel, STATUS_CODE
from ...schemas.machine import MachinePaingtionModel, AddMachineModel, RideMachineModel
from ...schemas.type import get_model
from ...service.MachineService import MachineService
from ...service.AreaService import AreaService
from ...service.RecordService import RecordService
from ...service.UserService import UserService
from ...core.auth import check_permission
from ...core.task import simulate_ev_ride
from ...utils.map_utils import is_machine_in_area, get_route_coordinates

router = APIRouter()


@router.post("/machine_list", summary="查询电动车列表", response_model=ReturnDataModel,
             dependencies=[Depends(check_permission)])
async def get_machine_list(query: MachinePaingtionModel = Depends(get_model(MachinePaingtionModel))):
    """
    获取电动车列表

    :param query: 查询参数，包括 page, page_size, status, area_id, machine_id
    :return: 电动车列表和总数
    """
    machine_service = MachineService()
    area_service = AreaService()

    # 获取电动车列表和总数
    machine_list, total = machine_service.get_machine_list(
        page=query.page,
        page_size=query.page_size,
        status=query.status,
        area_id=query.area_id,
        machine_id=query.machine_id
    )

    if total <= 0:
        return ReturnDataModel(
            data=[],
            total=0,
            success=True,
            code=STATUS_CODE["success"],
            message="查询成功，无电动车数据"
        )

    # 构建最终列表
    final_list = [
        {
            "create_time": machine.create_time,
            "update_time": machine.update_time,
            "machine_id": machine.machine_id,
            "machine_point": [machine.machine_point["longitude"], machine.machine_point["latitude"]],
            "machine_battery": machine.machine_battery,
            "area_name": area.area_name if (area := area_service.get_area_by_id(machine.area_id)) else "未知区域",
            "status": machine.status,
            "machine_photo": machine.machine_photo
        }
        for machine in machine_list
    ]

    return ReturnDataModel(
        data=final_list,
        total=total,
        success=True,
        code=STATUS_CODE["success"],
        message="查询成功"
    )


@router.post("/machine_add", summary="添加电动车", response_model=ReturnNoneDataModel,
             dependencies=[Depends(check_permission)])
async def add_machine(machine: AddMachineModel = Depends(get_model(AddMachineModel)),
                      user_info: Tuple[str, str] = Depends(check_permission)):
    """
    添加电动车

    :param machine: 电动车信息，包括 machine_point
    :param user_info: 用户信息 (user_id, role_id) 从 check_permission 获取
    :return: 添加结果
    """
    user_id, _ = user_info
    machine_service = MachineService()
    area_service = AreaService()

    # 获取所有区域并解析
    area_info_list = [
        {"area_id": area.area_id, "area_desc": ast.literal_eval(area.area_desc)}
        for area in area_service.get_all_area()
    ]

    # 判断电动车位置
    area_id = is_machine_in_area(machine.machine_point, area_info_list)
    if area_id == 0:
        return ReturnNoneDataModel(
            success=False,
            code=STATUS_CODE["error"],
            message="电动车不在区域内"
        )

    machine_service.create_machine(machine_point=machine.machine_point, area_id=area_id, user_id=user_id)
    return ReturnNoneDataModel(
        success=True,
        code=STATUS_CODE["success"],
        message="添加成功"
    )


@router.get("/machine_delete", summary="删除电动车", response_model=ReturnNoneDataModel,
            dependencies=[Depends(check_permission)])
async def delete_machine(machine_id: str):
    """
    删除电动车

    :param machine_id: 电动车ID
    :return: 删除结果
    """
    machine_service = MachineService()
    record_service = RecordService()

    machine_info = machine_service.get_machine_by_id(machine_id)
    if not machine_info:
        return ReturnNoneDataModel(
            success=False,
            code=STATUS_CODE["error"],
            message="该电动车不存在"
        )

    # 删除相关记录
    record_list = record_service.get_all_by_machine_id(machine_id)
    for record in record_list:
        record_service.delete(record)
    machine_service.delete(machine_info)

    return ReturnNoneDataModel(
        success=True,
        code=STATUS_CODE["success"],
        message="删除成功"
    )


@router.post("/start_ride", summary="开始骑行", response_model=ReturnNoneDataModel,
             dependencies=[Depends(check_permission)])
async def start_ride(ride: RideMachineModel = Depends(get_model(RideMachineModel)),
                     user_info: Tuple[str, str] = Depends(check_permission)):
    """
    开始骑行

    :param ride: 骑行信息，包括 machine_id, machine_origin, machine_destination
    :param user_info: 用户信息 (user_id, role_id) 从 check_permission 获取
    :return: 骑行任务结果
    """
    user_id, _ = user_info
    machine_service = MachineService()
    user_service = UserService()

    # 检查用户和电动车状态
    machine_info = machine_service.get_machine_by_id(ride.machine_id)
    user_info_obj = user_service.get_user_by_id(user_id)

    if not user_info_obj or user_info_obj.user_status != 1:
        return ReturnNoneDataModel(
            code=STATUS_CODE["warning"],
            message="用户不在可骑行状态",
            success=False
        )
    if not machine_info:
        return ReturnNoneDataModel(
            code=STATUS_CODE["error"],
            message="电动车不存在",
            success=False
        )
    if machine_info.machine_battery < 20:
        return ReturnNoneDataModel(
            code=STATUS_CODE["warning"],
            message="电动车电量不足，请换乘骑行",
            success=False
        )
    if machine_info.status != 1:
        return ReturnNoneDataModel(
            code=STATUS_CODE["warning"],
            message="电动车不在可骑行状态，请换乘骑行",
            success=False
        )

    # 更新状态
    machine_info.status = 0  # 骑行中
    user_info_obj.user_status = 2  # 用户骑行中
    machine_service.update(machine_info)
    user_service.update(user_info_obj)

    # 启动骑行任务
    route = get_route_coordinates(ride.machine_origin, ride.machine_destination)
    task = simulate_ev_ride.apply_async(args=[ride.machine_id, user_id, route])

    return ReturnNoneDataModel(
        code=STATUS_CODE["success"],
        message=f"开始骑行，任务ID为 {task.id}",
        success=True
    )
