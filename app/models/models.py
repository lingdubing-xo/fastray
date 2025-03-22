"""
@file: models.py
@author: lingdubing
@desc: 数据库模型文件
@character: utf-8
"""

from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from sqlalchemy import JSON, Column

class BasicModel(SQLModel):
    create_by: str = Field(description="创建者")
    create_time: datetime = Field(default=datetime.utcnow(), description="创建时间")
    update_by: str = Field(description="更新者")
    update_time: datetime = Field(default=datetime.utcnow(), description="更新时间")


class UserRoleLink(BasicModel, table=True):
    user_id: str = Field(foreign_key="user.user_id", primary_key=True, description="用户ID")
    role_id: str = Field(foreign_key="role.role_id", primary_key=True, description="角色ID")

    user: "User" = Relationship(back_populates="user_role_links")
    role: "Role" = Relationship(back_populates="user_links")


class RoleAccessLink(BasicModel, table=True):
    role_id: str = Field(foreign_key="role.role_id", primary_key=True, description="角色ID")
    access_id: str = Field(foreign_key="access.access_id", primary_key=True, description="权限ID")

    role: "Role" = Relationship(back_populates="access_links")
    access: "Access" = Relationship(back_populates="access_role_links")


class User(BasicModel, table=True):
    user_id: str = Field(primary_key=True, description="用户ID,用户的唯一标识")
    username: str = Field(description="用户名", index=True)
    password: str = Field(description="密码")
    user_status: int = Field(default=1, description="用户状态,0为禁用状态,1为可用状态,2表示正在骑行状态", index=True)

    # 附加的属性
    user_role_links: list[UserRoleLink] = Relationship(back_populates="user")
    records: list["Record"] = Relationship(back_populates="user")


class Role(BasicModel, table=True):
    role_id: str = Field(primary_key=True, description="角色ID,角色的唯一标识")
    role_name: str = Field(description="角色名")
    role_desc: str | None = Field(description="角色描述", default=None)

    user_links: list[UserRoleLink] = Relationship(back_populates="role")
    access_links: list[RoleAccessLink] = Relationship(back_populates="role")


class Access(BasicModel, table=True):
    access_id: str = Field(primary_key=True, description="权限ID,权限的唯一标识")
    access_name: str = Field(description="权限名")
    access_desc: str | None = Field(description="权限描述", default=None)
    access_url: str | None = Field(description="权限URL", default=None)
    parent_id: str | None = Field(description="父亲ID", default=None)
    is_menu: bool = Field(description="是否为菜单", default=False)
    is_verify: bool = Field(description="是否需要验证", default=True)

    access_role_links: list[RoleAccessLink] = Relationship(back_populates="access")


class Machine(BasicModel, table=True):
    machine_id: str = Field(primary_key=True, description="电动车ID,电动车的唯一标识")
    machine_point: dict | None = Field(default=None, description="电动车位置", sa_column=Column(JSON))
    machine_battery: int = Field(default=100, description="电动车电量")
    status: int = Field(default=1, description="电动车状态,0为正在骑行中,1为空闲状态,2为损坏,3为正在停止")
    machine_photo: str | None = Field(default=None, description="电动车照片")

    area_id: str = Field(foreign_key="area.area_id", description="区域ID")
    area: "Area" = Relationship(back_populates="machines")
    records: list["Record"] = Relationship(back_populates="machine")


class Area(BasicModel, table=True):
    area_id: str = Field(primary_key=True, description="区域ID,区域的唯一标识")
    area_name: str | None = Field(default=None, description="区域名")
    area_desc: str | None = Field(default=None, description="区域描述")

    machines: list[Machine] = Relationship(back_populates="area")


class Record(BasicModel, table=True):
    record_id: str = Field(primary_key=True, description="记录ID,记录的唯一标识")
    start_time: datetime | None = Field(default=None, description="开始时间")
    end_time: datetime | None = Field(default=datetime.utcnow(), description="结束时间")
    stop_time: int = Field(default=0, description="停车时间")
    consume_battery: int = Field(default=0, description="消耗电量")
    tracejectory: dict | None = Field(default=None, description="轨迹", sa_column=Column(JSON))

    # 附加属性
    user_id: str = Field(foreign_key="user.user_id", description="用户ID")
    user: User = Relationship(back_populates="records")
    machine_id: str = Field(foreign_key="machine.machine_id", description="电动车ID")
    machine: Machine = Relationship(back_populates="records")



