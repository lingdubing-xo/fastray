"""
@file: area.py
@author: lingdubing
@desc: 操作区域行为的接口层
@character: utf-8
"""

from fastapi import APIRouter, Depends
from ...schemas.response import ReturnDataModel, STATUS_CODE
from ...schemas.type import get_model
from ...core.auth import check_permission
from ...schemas.area import AreaPaingtionModel
from ...service.AreaService import AreaService

router = APIRouter()


@router.post("/area_list", summary="获取区域列表", response_model=ReturnDataModel,
             dependencies=[Depends(check_permission)])
async def get_area_list(query: AreaPaingtionModel = Depends(get_model(AreaPaingtionModel))):
    """
    获取区域列表

    :param query: 分页查询参数，包括 page 和 page_size
    :return: 区域列表和总数
    """
    area_service = AreaService()

    # 获取区域列表和总数
    area_list, total = area_service.get_paginated(page=query.page, page_size=query.page_size)

    if total <= 0:
        return ReturnDataModel(
            code=STATUS_CODE["success"],
            message="获取区域列表成功，无区域数据",
            success=True,
            data=[],
            total=0
        )

    # 构建最终区域列表
    final_list = [
        {
            "area_id": area.area_id,
            "area_name": area.area_name,
            "area_desc": area.area_desc,
            "create_time": area.create_time,
            "update_time": area.update_time
        }
        for area in area_list
    ]

    return ReturnDataModel(
        code=STATUS_CODE["success"],
        message="获取区域列表成功",
        success=True,
        data=final_list,
        total=total
    )
