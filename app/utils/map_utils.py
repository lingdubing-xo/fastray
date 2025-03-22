"""
@file: map_utils.py
@author: lingdubing
@desc: 地图工具类
@character: utf-8
"""

import math
import requests
from config import settings
from shapely.geometry import Point, Polygon



def is_machine_in_area(machine_point, area_info_list):
    """
    判断电动车是否在合法区域内
    :param machine_point: 电动车的经纬度信息 {longitude, latitude}
    :param area_info_list: 所有区域的经纬度信息
    :return: True - 在合法区域，False - 不在合法区域
    """
    for area_info in area_info_list:
        area_polygon = Polygon(area_info["area_desc"])
        machine_point_obj = Point(machine_point["longitude"], machine_point["latitude"])
        if area_polygon.contains(machine_point_obj):
            return area_info["area_id"]
    return 0


def get_route_coordinates(origin, destination):
    """
    调用高德API获取路径规划，并提取中间的5个坐标点。
    """
    url = settings.map_url

    # 将起点和终点从字典格式转换为经纬度字符串格式
    origin_str = f"{origin['longitude']},{origin['latitude']}"
    destination_str = f"{destination['longitude']},{destination['latitude']}"

    params = {
        "origin": origin_str,  # 起点坐标
        "destination": destination_str,  # 终点坐标
        "key": settings.map_key,  # 高德API密钥
        "extensions": "base"  # 返回基本信息
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] != "1":
        print("请求失败:", data.get("info", "未知错误"))
        return None

    # 提取路径的所有坐标点
    steps = data["route"]["paths"][0]["steps"]  # 获取路径中的步骤
    coordinates = []
    for step in steps:
        polyline = step["polyline"]  # 每个步骤中的坐标串
        coords = polyline.split(";")  # 将坐标串分割为列表
        coordinates.extend(coords)  # 添加到总坐标列表中

    total_points = len(coordinates)
    if total_points < 1:
        return coordinates  # 如果没有坐标点，返回空
    # 动态计算需要返回的坐标点数量，至少返回1个点
    num_points_to_return = max(1, math.ceil(total_points / 5))  # 计算需要的坐标点数（向上取整）
    # 计算每个点的间隔，向上取整
    step_size = math.ceil(total_points / num_points_to_return)
    # 返回的坐标经纬度列表
    return [coordinates[i * step_size] for i in range(num_points_to_return)]
