"""
@release: fsray-api-beta
@file: sms_utils.py
@desc：验证码生成和发送的工具类
@character: utf-8
"""

import random
from config import settings
import requests


def generate_code(n: int = 6) -> str:
    """
    生成验证码
    :param n: 验证码长度，默认为6
    :return: 随机验证码字符串
    """
    code = ""
    for i in range(n):
        num = random.randint(0, 9)
        upper_letter = chr(random.randint(65, 90))  # 大写字母 A-Z
        lower_letter = chr(random.randint(97, 122))  # 小写字母 a-z
        s = str(random.choice([num, upper_letter, lower_letter]))
        code += s
    return code


def send_code(phone: str, code: str) -> dict:
    """
    发送验证码
    :param phone: 手机号
    :param code: 验证码
    :return: 发送结果（JSON格式）
    """
    username = settings.msg_user
    password = settings.msg_password

    content = f"【FASTRAY】该手机正在进行短信验证的服务，您的验证码是{code}，如非本人请勿理会。"
    url = f"http://api.smsbao.com/sms?u={username}&p={password}&m={phone}&c={content}"

    response = requests.get(url)
    result = response.json()
    return result
