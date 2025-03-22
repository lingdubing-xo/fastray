"""
@file: BaseService.py
@author: lingdubing
@desc: 基础设施文件
@character: utf-8
"""

from typing import Generic, TypeVar, Optional, Iterator, Tuple
from sqlmodel import Session, select, SQLModel, func
from contextlib import contextmanager
from ..database.mysql import engine
from typing import Dict, Union

T = TypeVar("T", bound=SQLModel)


class BaseService(Generic[T]):
    def __init__(self, model: type[T], id_field: Optional[str] = None):
        self.model = model
        self.pk_fields = self.model.__table__.primary_key.columns.keys()
        self.id_field = id_field or self.pk_fields[0] if len(self.pk_fields) == 1 else None

    @contextmanager
    def get_session(self) -> Iterator[Session]:
        session = Session(engine, expire_on_commit=False)
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def get_by_id(self, id_value: Union[Dict[str, any], Tuple, any]) -> Optional[T]:
        with self.get_session() as session:
            if isinstance(id_value, dict):
                # 复合主键：键值对方式
                statement = select(self.model)
                for key, value in id_value.items():
                    if key not in self.pk_fields:
                        raise ValueError(f"Invalid primary key field '{key}' for model {self.model.__name__}")
                    statement = statement.where(getattr(self.model, key) == value)
                return session.exec(statement).first()
            elif isinstance(id_value, tuple):
                # 复合主键：元组方式
                if len(id_value) != len(self.pk_fields):
                    raise ValueError(
                        f"Expected {len(self.pk_fields)} values for composite key, got {len(id_value)}"
                    )
                return session.get(self.model, id_value)
            else:
                # 单一主键
                if len(self.pk_fields) > 1:
                    raise ValueError(f"Model {self.model.__name__} has composite key, use dict or tuple")
                return session.get(self.model, id_value)

    def create(self, instance: T) -> T:
        with self.get_session() as session:
            session.add(instance)
            session.commit()
            session.refresh(instance)
            return instance

    def update(self, instance: T) -> T:
        with self.get_session() as session:
            session.add(instance)
            session.commit()
            session.refresh(instance)
            return instance

    def delete(self, instance: T) -> None:
        with self.get_session() as session:
            session.delete(instance)

    def get_paginated(self, page: int, page_size: int, filters: Optional[list] = None) -> Tuple[list[T], int]:
        offset = (page - 1) * page_size
        with self.get_session() as session:
            # 查询分页数据
            statement = select(self.model).offset(offset).limit(page_size)
            if filters:
                for filter_ in filters:
                    statement = statement.where(filter_)
            items = session.exec(statement).all()

            # 查询所有数据总数
            total_statement = select(func.count()).select_from(self.model)
            total = session.exec(total_statement).one()

            return items, total
