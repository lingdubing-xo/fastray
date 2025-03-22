"""
@file: record.py
@author: lingdubing
@desc: 操作记录行为的接口层
@character: utf-8
"""

from fastapi import APIRouter, Depends
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from typing import Tuple
from ...schemas.response import ReturnDataModel, STATUS_CODE
from ...schemas.record import RecordPaingtionModel
from ...schemas.type import get_model
from ...core.auth import check_permission
from ...service.RecordService import RecordService
from ...service.UserService import UserService
from ...service.AreaService import AreaService
from ...service.MachineService import MachineService




router = APIRouter()



@router.post("/get_record_list", summary="获取订单列表", response_model=ReturnDataModel,
             dependencies=[Depends(check_permission)])
async def get_record_list(query: RecordPaingtionModel = Depends(get_model(RecordPaingtionModel)),
                          user_info: Tuple[str, str] = Depends(check_permission)):
    """
    获取订单列表

    :param query: 分页查询参数，包括 page, page_size, time_range, record_id
    :param user_info: 用户信息 (user_id, role_id) 从 check_permission 获取
    :return: 订单列表和总数
    """
    # 创建服务实例
    record_service = RecordService()
    user_service = UserService()

    # 计算时间筛选的开始时间
    time_ranges = {
        "3d": timedelta(days=3),
        "1w": timedelta(weeks=1),
        "1m": timedelta(days=30)
    }
    start_time = datetime.now() - time_ranges.get(query.time_range, timedelta(0)) if query.time_range else None
    user_id, role_id = user_info

    # 获取订单列表和总数
    record_list, total = record_service.get_record_list(
        page=query.page,
        page_size=query.page_size,
        start_time=start_time,
        record_id=query.record_id,
        user_id=user_id,
        role_id=role_id
    )

    if total <= 0:
        return ReturnDataModel(
            code=STATUS_CODE["error"],
            message="查询失败，无订单数据",
            success=False,
            data=[],
            total=0
        )

    # 构建最终订单列表
    final_list = [
        {
            "create_time": record.create_time,
            "update_time": record.update_time,
            "record_id": record.record_id,
            "start_time": record.start_time,
            "end_time": record.end_time,
            "stop_time": record.stop_time,
            "consume_battery": record.consume_battery,
            "username": user_service.get_user_by_id(record.user_id).username if record.user_id else None,
            "tracejectory": record.tracejectory,
            "machine_id": record.machine_id
        }
        for record in record_list
    ]

    return ReturnDataModel(
        code=STATUS_CODE["success"],
        message="获取订单列表成功",
        success=True,
        data=final_list,
        total=total
    )




@router.get('/get_anaylze', summary="获取统计信息", response_model=ReturnDataModel,
            dependencies=[Depends(check_permission)])
async def get_anaylze():
    """

    :return: 统计数据字典
    """
    # 创建服务实例
    user_service = UserService()
    record_service = RecordService()
    machine_service = MachineService()
    area_service = AreaService()

    # 获取时间范围
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())  # 本周一
    start_of_last_week = start_of_week - timedelta(days=7)  # 上周一
    end_of_last_week = start_of_last_week + timedelta(days=6)  # 上周日

    # 一次性获取所有数据
    all_users = user_service.get_all()
    all_machines = machine_service.get_all()
    all_areas = area_service.get_all()
    last_week_records = record_service.get_records_in_range(start_of_last_week, start_of_week)
    this_week_records = record_service.get_records_in_range(start_of_week, datetime.now())

    # 初始化结果
    analyze_result = {
        "user_count": len(all_users),
        "all_machine_count": len(all_machines),
        "riding_machine_count": sum(1 for m in all_machines if m.status == 0),
        "illegal_machine_count": sum(1 for m in all_machines if m.status == 2),
        "all_area_count": len(all_areas),
        "area_machine_count": {},
        "week_order_count": [0] * 7,
        "week_order_count_last_week": [0] * 7,
        "top_10_machines": [],
        "top_10_users": []
    }

    # 区域电动车数量
    area_counts = defaultdict(int)
    for machine in all_machines:
        if machine.area_id:
            area_counts[machine.area_id] += 1
    analyze_result["area_machine_count"] = dict(area_counts)

    # 本周订单统计
    for record in this_week_records:
        if record.start_time:
            day_offset = (record.start_time - start_of_week).days
            if 0 <= day_offset < 7:
                analyze_result["week_order_count"][day_offset] += 1

    # 上周订单统计及前十排名
    machine_counts = Counter()
    user_counts = Counter()
    for record in last_week_records:
        if record.start_time:
            day_offset = (record.start_time - start_of_last_week).days
            if 0 <= day_offset < 7:
                analyze_result["week_order_count_last_week"][day_offset] += 1
        if record.machine_id:
            machine_counts[record.machine_id] += 1
        if record.user_id:
            user_counts[record.user_id] += 1

    analyze_result["top_10_machines"] = machine_counts.most_common(10)
    analyze_result["top_10_users"] = user_counts.most_common(10)

    return ReturnDataModel(
        code=STATUS_CODE["success"],
        message="获取统计信息成功",
        success=True,
        data=analyze_result,
        total=0
    )
