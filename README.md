# FastRay

## 项目介绍
一个使用Python FastAPI 框架搭建的 Python web 应用。
提供完善的鉴权系统和管理系统, 该项目旨在为电动车(或其他)管理提供一个切实可行的方案

## 关键技术栈

- **Python**: 3.8+ 
- **FastAPI**: 高性能异步 Web 框架
- **SQLModel**: SQLModel 是一个用于从 Python 代码与 SQL 数据库 交互的库
- **Celery** 异步任务框架
- **MySQL/Redis**: 数据库支持
- **JWT**: JSON Web Token 用于身份验证
- **Pydantic**: 数据验证和设置管理
- **Uvicorn**: ASGI 服务器


## 项目结构

```
fastray/
├── app/                        # 应用主目录
│   ├── api/                    # API 接口和路由
│   │   ├── endpoints/          # API 端点实现
│   │   └── views/              # 视图函数
│   ├── core/                   # 核心功能模块
│   │   ├── auth.py             # 鉴权模块
│   │   ├── events.py           # 应用事件处理（启动、关闭等）
│   │   ├── exceptions.py       # 自定义异常类
│   │   ├── log_midderware.py   # 日志中间件
│   │   ├── router.py           # 路由聚合
│   │   ├── task.py             # 异步任务
│   ├── database/               # 日志配置
│   │   ├── mysql/              # mysql初始化
│   │   ├── redis/              # redis初始化
│   ├── models/                 # 数据库模型
│   │   ├── models/             # 模型文件
│   ├── schemas/                # 数据验证模型
│   ├── services/               # 业务逻辑
│   └── utils/                  # 工具函数
│       ├── crypto_utils.py/    # 加密工具
│       ├── map_utils/          # 地图工具
│       ├── sms_utils/          # 验证码生成和发送的工具类
├── logs/                       # 日志文件目录
├── resources/                  # 资源文件目录
│   ├── static/                 # 静态资源文件
│   └── templates/              # HTML 模板文件
├── config.py                   # 配置文件
├── main.py                     # 应用入口
├── requirements.txt            # 项目依赖
├── pyproject.toml              # 依赖管理文件
└── README.md                   # md文档
```

## 数据架构设计
FastRay 采用了传统的角色-权限-用户模型设计

## 核心功能

- 用户,电动车,区域状态管理
- 用户认证与授权
- 异步任务处理
- 骑行记录和数据统计
- 地图导航和路径规划
- 支持form和json两种提交方式


## 配置文件

项目的主要配置位于 `config.py`：
读取.env文件
下面是例子空为自己的,其他可默认
```.env
APP_DEBUG=False
VERSION=1.0.0
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_PORT=3306
MYSQL_IP=127.0.0.1
MYSQL_DATABASE=
CACHE_HOST=127.0.0.1
CACHE_PORT=6379
TASK_CACHE_DB=0
CODE_CACHE_DB=1
TOKEN_CACHE_DB=2
MSG_USER=
MSG_PASSWORD=
JWT_SECRET_KEY=
JWT_ALGORITHM=
MAP_URL=https://restapi.amap.com/v3/direction/driving
MAP_KEY=
CELERY_BROKER=redis://127.0.0.1:6379/0
MINIO_URL=81.70.177.87:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
MINIO_SECURE=False
BUCKET_NAME=machinepicture
LOG_DIR=logs
LOG_LEVEL=INFO
```

## 开发环境配置

1. 克隆项目并安装依赖：
```bash
git clone <repository-url>
cd fastray
.venv/bin/activate
uv sync(需安装uv)
```
2. 配置 `.env`：
3. 运行项目：
```bash
uv run uvicorn main:app --reload
```
访问 http://localhost:8000/fsray/index 查看首页。
访问 http://localhost:8000/docs 查看 API 文档。

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。

## 联系方式

Email: 3189377462@qq.com

