"""
@file: RecordService.py
@author: lingdubing
@desc: 记录设施文件
@character: utf-8
"""

from ..models.models import Record
from .BaseService import BaseService
from sqlmodel import select
from ..utils.crypto_utils import generate_uuid
from typing import Optional, Tuple, List
from datetime import datetime

class RecordService(BaseService[Record]):
    """记录服务类"""

    def __init__(self):
        """
        初始化记录服务
        """
        super().__init__(Record, id_field="record_id")

    def get_all_by_machine_id(self, machine_id: str) -> List[Record]:
        """根据机器ID获取所有记录"""
        with self.get_session() as session:
            statement = select(Record).where(Record.machine_id == machine_id)
            return session.exec(statement).all()

    def create_ride_record(self, machine_id: str, user_id: str, start_time: datetime, end_time: datetime,
                           tracejectory: List[Tuple[float, float]], consume_battery: int) -> Record:
        """
        创建骑行记录

        :param machine_id: 电动车ID
        :param user_id: 用户ID
        :param start_time: 开始时间
        :param end_time: 结束时间
        :param tracejectory: 骑行轨迹
        :param consume_battery: 消耗电量
        :return: 创建的记录对象
        """
        record = Record(
            machine_id=machine_id,
            user_id=user_id,
            start_time=start_time,
            end_time=end_time,
            tracejectory=tracejectory,
            stop_time=0,
            consume_battery=consume_battery,
            record_id=generate_uuid(),
            update_by=user_id,
            create_by=user_id
        )
        return self.create(record)

    def get_record_list(self, page: int, page_size: int,
                        record_id: Optional[str] = None, user_id: Optional[str] = None,
                        role_id: Optional[str] = None, start_time: Optional[datetime] = None,
                        end_time: Optional[datetime] = None) -> Tuple[List[Record], int]:
        """获取记录列表（分页）"""
        filters = []

        # 添加过滤条件
        if role_id is not None and int(role_id) not in (0, 1):
            filters.append(Record.user_id == user_id)
        if start_time is not None:
            filters.append(Record.create_time >= start_time)
        if end_time is not None:
            filters.append(Record.create_time <= end_time)
        if record_id is not None:
            filters.append(Record.record_id == record_id)

        # 获取分页数据
        return self.get_paginated(page, page_size, filters=filters)
