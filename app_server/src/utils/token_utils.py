#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :token_utils.py
@说明        :
@时间        :2020/07/28 15:59:47
@作者        :Riven
@版本        :1.0.0
'''

import time
import base64
import hmac

import sys
sys.path.append('.')
from app_server.src.utils.string_utils import random_string

def generate_token(key, expire=60*60*24):
    """
    @Args:
        key: str (用户给定的key，需要用户保存以便之后验证token,每次产生token时的key 都可以是同一个key)
        expire: int(最大有效时间，单位为s)
    @Return:
        state: str
    :param key:
    :param expire:
    :return:
    """
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode('utf-8')
    sha1_tshex_str = hmac.new(key.encode('utf-8'), ts_byte, 'sha1').hexdigest()
    token = ts_str + ':' + sha1_tshex_str
    b64_token = base64.urlsafe_b64encode(token.encode('utf-8'))

    return b64_token.decode('utf-8')


def verify_token(key, token):
    """
    @Args:
        key: str
        token: str
    @Returns:
        boolean
    :param key:
    :param token:
    :return:
    """
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False

    ts_str = token_list[0]
    if float(ts_str) < time.time():
        return False

    known_sha1_testr = token_list[1]
    sha1 = hmac.new(key.encode('utf-8'), ts_str.encode('utf-8'), 'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_testr:
        return False

    return True

# 生成随机字符串
def random_token(from_text=None,len=32):
    return random_string(from_text, len)

