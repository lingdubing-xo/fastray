"""
@file: config.py
@author: lingdubing
@desc: 项目配置类，管理环境变量和应用设置
@character: utf-8
"""

import os
from typing import List, Dict
from celery import Celery
from dotenv import load_dotenv, find_dotenv
from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

load_dotenv(find_dotenv(), override=True)

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=find_dotenv(),
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    app_debug: bool = Field(default=False, description="调试模式，生产环境应关闭", env="APP_DEBUG")
    version: str = Field(description="版本号", env="VERSION")
    project_name: str = "FastRay"

    # === 日志 配置 ===
    log_dir: Path = Field(default=Path("log"), env="LOG_DIR", description="日志存储目录")
    log_level: str = Field(default="INFO", env="LOG_LEVEL", description="日志级别")
    log_format: str = Field(default="%(asctime)s - %(levelname)s - %(message)s",
                            description="日志格式")
    log_datefmt: str = Field(default="%Y-%m-%d %H:%M:%S", description="日志时间格式")

    @computed_field
    @property
    def resources_dir(self) -> str:
        """资源目录，动态计算"""
        return os.path.join(BASE_DIR, "resources")

    @computed_field
    @property
    def static_dir(self) -> str:
        """静态目录，基于 resources_dir"""
        return os.path.join(self.resources_dir, "static")

    @computed_field
    @property
    def template_dir(self) -> str:
        """模板目录，基于 static_dir"""
        return os.path.join(self.resources_dir, "templates")

    cors_origins: List[str] = Field(
        default_factory=lambda: ["http://127.0.0.1", "http://localhost", "http://localhost:8080"],
        description="允许的CORS来源，仅限本地访问",
    )
    cors_allow_credentials: bool = True
    cors_allow_methods: List[str] = Field(default_factory=lambda: ["GET", "POST", "PUT", "DELETE"])
    cors_allow_headers: List[str] = Field(default_factory=lambda: ["Authorization", "Content-Type"])

    # === MySQL 配置 ===
    mysql_user: str = Field(default="root", env="MYSQL_USER")
    mysql_password: str = Field(..., env="MYSQL_PASSWORD")
    mysql_port: int = Field(default=3306,env="MYSQL_PORT")
    mysql_ip: str = Field(default="127.0.0.1", env="MYSQL_IP")
    mysql_database: str = Field(env="MYSQL_DATABASE")

    # === Redis 配置 ===
    cache_host: str = Field(default="127.0.0.1", env="CACHE_HOST")
    cache_port: int = Field(default=6379, ge=1, le=65535, env="CACHE_PORT")

    # === 骑行任务缓存 ===
    task_cache_db: int = Field(default=0, env="TASK_CACHE_DB")
    code_cache_db: int = Field(default=1, env="CODE_CACHE_DB")
    token_cache_db: int =  Field(default=2, env="TOKEN_CACHE_DB")

    # === 短信服务配置 ===
    msg_user: str = Field(env="MSG_USER")
    msg_password: str = Field(..., env="MSG_PASSWORD")
    msg_status_codes: Dict[str, str] = Field(
        default_factory=lambda: {
            "0": "短信发送成功",
            "-1": "参数不全",
            "-2": "服务器不支持curl或fsocket",
            "30": "密码错误",
            "40": "账号不存在",
            "41": "余额不足",
            "42": "账户已过期",
            "43": "IP地址限制",
            "50": "内容含有敏感词",
            "51": "手机号码不正确",
        },
        description="短信服务状态码映射",
    )

    # === JWT 配置 ===
    jwt_secret_key: str = Field(..., env="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(..., env="JWT_ALGORITHM")

    # === 角色配置 ===
    role_dict: Dict[str, int] = Field(
        default_factory=lambda: {"admin": 0, "staff": 1, "user": 2},
        description="角色权限映射",
    )

    # === 高德地图配置 ===
    map_url: str = Field(..., env="MAP_URL")
    map_key: str = Field(..., env="MAP_KEY")

    # === Celery 配置 ===
    celery_broker: str = Field(..., env="CELERY_BROKER")

    @computed_field
    @property
    def celery_app(self) -> Celery:
        """Celery 实例，动态创建并配置"""
        app = Celery("fsray-tasks", broker=self.celery_broker)
        app.conf.update(timezone="Asia/Shanghai")
        return app

    # === Minio 配置 ===
    minio_url: str = Field(..., env="MINIO_URL")
    minio_access_key: str = Field(..., env="MINIO_ACCESS_KEY")
    minio_secret_key: str = Field(..., env="MINIO_SECRET_KEY")
    minio_secure: bool = Field(env="MINIO_SECURE")
    bucket_name: str = Field(env="BUCKET_NAME")



settings = Config()
