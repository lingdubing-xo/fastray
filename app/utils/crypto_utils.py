"""
@release: fsray-api-beta
@file: crypto_utils.py
@desc：加密和密码相关的工具类
@character: utf-8
"""

import uuid
from passlib.handlers.pbkdf2 import pbkdf2_sha256
import datetime
from config import settings
import jwt


def generate_uuid() -> str:
    """
    生成uuid
    :return: uuid字符串
    """
    return str(uuid.uuid4())


def en_password(psw: str) -> str:
    """
    加密密码
    :param psw: 用户输入的密码
    :return: 用户加密后的密码
    """
    password = pbkdf2_sha256.hash(psw)
    return password


def check_password(user_psw: str, e_password: str) -> bool:
    """
    验证密码
    :param user_psw: 用户输入的密码
    :param e_password: 数据库的密码
    :return: 是否匹配
    """
    return pbkdf2_sha256.verify(user_psw, e_password)

def generate_token(phone: str):
    timestamp = int(datetime.datetime.utcnow().timestamp())  # 当前时间戳
    # 计算过期时间戳（秒级）
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)  # 当前时间戳加上一小时

    data = {'username': phone, 'exp': expiration_time, 'timestamp': timestamp}

    token = jwt.encode(payload=data, key=settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return token
