"""
@file: Task.py
@author: lingdubing
@desc: 电动车任务类
@character: utf-8
"""

import ast
from datetime import datetime
from typing import List, Tuple
from config import settings
from ..service.MachineService import MachineService
from ..service.UserService import UserService
from ..service.AreaService import AreaService
from ..service.RecordService import RecordService
from ..utils.map_utils import is_machine_in_area

celery_app = settings.celery_app

@celery_app.task
def simulate_ev_ride(machine_id: str, user_id: str, route: List[str]) -> None:
    """
    模拟电动车骑行的任务，更新电动车位置和状态。

    :param machine_id: 电动车ID
    :param user_id: 用户ID
    :param route: 骑行路线，格式为 ["经度,纬度", ...]
    """
    # 创建服务实例
    machine_service = MachineService()
    user_service = UserService()
    area_service = AreaService()
    record_service = RecordService()

    # 初始化骑行数据
    start_time = datetime.utcnow()
    tracejectory: List[Tuple[float, float]] = []

    print(f"电动车 {machine_id} 的骑行任务开始，用户 {user_id} 从起点出发。")

    # 获取初始电动车信息
    machine_info = machine_service.get_machine_by_id(machine_id)
    if not machine_info:
        print(f"错误：电动车 {machine_id} 不存在")
        return

    # 模拟骑行过程
    for point in route:
        longitude, latitude = map(float, point.split(","))
        machine_info.machine_point = {"longitude": longitude, "latitude": latitude}
        machine_service.update(machine_info)
        tracejectory.append((longitude, latitude))
        # time.sleep(2)  # 模拟延迟，生产环境中可调整或移除

    # 更新用户状态
    user_info = user_service.get_user_by_id(user_id)
    if user_info:
        user_info.user_status = 1  # 表示骑行中
        user_service.update(user_info)
    else:
        print(f"警告：用户 {user_id} 不存在")

    # 更新电动车结束状态
    machine_info.machine_battery -= len(tracejectory)  # 每点消耗 1% 电量
    machine_info.update_time = datetime.utcnow()

    # 获取所有非异常区域
    area_list = [
        {"area_id": area.area_id, "area_desc": ast.literal_eval(area.area_desc)}
        for area in area_service.get_all_area()
    ]

    # 判断终点位置
    end_point = {
        "longitude": float(route[-1].split(",")[0]),
        "latitude": float(route[-1].split(",")[1])
    }
    area_id = is_machine_in_area(end_point, area_list)
    machine_info.status = 2 if area_id == 0 else 1
    machine_info.area_id = area_id
    machine_service.update(machine_info)

    end_time = datetime.utcnow()
    record_service.create_ride_record(
        machine_id=machine_id,
        user_id=user_id,
        start_time=start_time,
        end_time=end_time,
        tracejectory=tracejectory,
        consume_battery=len(tracejectory)
    )

    print(f"骑行结束，电动车 {machine_id} 最终位置：({end_point['longitude']}, {end_point['latitude']})，"
          f"电池剩余：{machine_info.machine_battery}%")
