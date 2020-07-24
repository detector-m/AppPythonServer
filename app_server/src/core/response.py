#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :response.py
@说明        :
@时间        :2020/07/24 11:52:52
@作者        :Riven
@版本        :1.0.0
'''

from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

def response(code=200, data=None, error=None, msg=None):
    '''
    :param code: 状态码
    :param data: 返回数据
    :param error: 错误信息
    :param msg: 提示信息
    '''

    if code is not None and code >= 400:
        error = HTTP_STATUS_CODES.get(code, "unknown error")

    pay_load = {
        "code": code, 
        "data": data, 
        "err": error,
        "message": msg or HTTP_STATUS_CODES.get(code, "unknown error")
    }

    # with ttt_app.app_context():
    _res = jsonify(pay_load)
    _res.status_code = code

    return _res
