"""
@file: user.py
@author: lingdubing
@desc: 可复用的类型定义
@character: utf-8
"""

from typing import Annotated, Any, Type, TypeVar
from fastapi import Query, HTTPException, Request, Depends
from pydantic import BaseModel, Field
from .response import STATUS_CODE


# 手机号类型（中国大陆11位）
PhoneNumber = Annotated[
    str,
    Query(
        ...,
        description="用户手机号",
        min_length=11,
        max_length=11,
        regex=r"^1[3-9]\d{9}$",
    )
]

# UUID 类型
Uuid = Annotated[
    str,
    Query(
        ...,
        description="UUID格式的唯一标识符",
        regex=r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
    )
]


class FormJsonBase(BaseModel):
    """支持JSON和表单数据的通用基类"""

    @classmethod
    def as_form(cls, form_data: dict):
        """
        默认的表单解析方法，子类可覆盖以定义特定字段
        :param form_data: 表单数据
        :return: 模型实例
        """
        return cls(**form_data)

    class Config:
        from_attributes = True  # 允许从数据库对象转换
        # 允许任意类型（如 dict），以支持 JSON 字段
        arbitrary_types_allowed = True


async def parse_request_data(request: Request, model_class: type) -> Any:
    """
    通用的请求数据解析函数，支持JSON和表单数据

    :param request: HTTP请求对象
    :param model_class: 要解析的目标Pydantic模型类
    :return: 解析后的模型实例
    """
    content_type = request.headers.get("Content-Type", "").lower()

    if "application/json" in content_type:
        data = await request.json()
        try:
            return model_class(**data)
        except ValueError as e:
            raise HTTPException(status_code=STATUS_CODE["unprocessable entity"], detail=f"Invalid JSON data: {str(e)}")
    elif "application/x-www-form-urlencoded" in content_type or "multipart/form-data" in content_type:
        form_data = await request.form()
        form_dict = {key: value for key, value in form_data.items()}
        try:
            return model_class.as_form(form_dict)
        except ValueError as e:
            raise HTTPException(status_code=STATUS_CODE["unprocessable entity"], detail=f"Invalid form data: {str(e)}")
    else:
        raise HTTPException(status_code=STATUS_CODE["unsupported media type"],
                            detail="Unsupported Media Type: Use application/json, application/x-www-form-urlencoded, or multipart/form-data")

T = TypeVar("T", bound=FormJsonBase)

def get_model(model_class: Type[T]):
    async def _get_model(request: Request) -> T:
        return await parse_request_data(request, model_class)
    return _get_model

class PaginationBase(FormJsonBase):
    page: int = Field(1, description="页码")
    page_size: int = Field(10, description="每页数量")


