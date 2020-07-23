#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :error.py
@说明        :
@时间        :2020/07/22 17:45:23
@作者        :Riven
@版本        :1.0.0
'''

__author__ = 'Riven'


from flask import request, json, Flask
from werkzeug.exceptions import HTTPException

import sys
sys.path.append('.')
from app_server.src.core.core_helper import jsonify

def handle_error(app: Flask):
    @app.errorhandler(Exception)
    def _handle_error(e):
        if isinstance(e, APIException):
            return e
        elif isinstance(e, HTTPException):
            return APIException(code=e.code, error_code=1007, msg=e.description)
        # 暂未加入数据库功能
        # elif isinstance(e, IntegrityError) and 'Duplicate entry' in e.orig.errmsg:
        #     return RepeatException(msg='数据的unique字段重复')
        else:
            if not app.config['DEBUG']:
                # 未知错误(统一为服务端异常)
                return ServerError()
            else:
                raise e

class APIException(HTTPException):
    code = 500 # http 状态码
    msg = '服务器未知错误'  # 异常信息
    error_code = 999 # 约定的异常码

    def __init__(self, code=None, error_code=None, msg=None, headers=None):
        if code:
            self.code = code
        
        if error_code:
            self.error_code = error_code
        
        if msg:
            self.msg = msg
        
        # super(APIException, self).__init__()
        super().__init__()

    
    def get_body(self, environ=None):
        body = dict(msg=self.msg, error_code=self.error_code, request_url=request.method + ' ' + self.get_url_no_param())

        # 返回文本
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [('Content-type', 'application/json; charset=utf-8')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')[0]

        return main_path

############################################
##########    基础类错误(0~9999)   ##########
############################################
class Success(APIException):
    '''
    0/200: 查询成功
    1/201: 创建 | 更新成功
    2/203: 删除成功
    '''
    code = 200
    error_code = 0
    data = None
    msg = '成功'

    def __init__(self, data=None, code=None, error_code=None, msg=None):
        if data:
            self.data = jsonify(data)

        if error_code == 1:
            code = code if code else 201
            msg = msg if msg else '创建 | 更新成功'
        elif error_code == 2:
            code = code if code else 202
            msg = msg if msg else '删除成功'

        super().__init__(code, error_code, msg)

    def get_body(self, environ=None):
        body = dict(error_code=self.error_code, msg=self.msg, data=self.data)
        text = json.dumps(body) 
        
        return text

class ServerError(APIException):
    code = 500
    error_code = 999
    msg = '服务器端异常'

class Failed(APIException):
    code = 400
    error_code = 9999
    msg = '失败'

############################################
########## 基础类错误(11000~12000) ##########
############################################

##########  权限相关(10000~10100)  ##########
class AuthFailed(APIException):
    code = 401
    error_code = 10000
    msg = '授权失败'


class Forbidden(APIException):
    code = 403
    error_code = 10010
    msg = '权限不足，禁止访问'


##########  查询相关(10100~10200)  ##########
class NotFound(APIException):
    code = 404  # http 状态码
    error_code = 10100  # 约定的异常码
    msg = '未查询到数据'  # 异常信息


class RepeatException(APIException):
    code = 400
    error_code = 10110
    msg = '重复数据'


class ParameterException(APIException):
    code = 400
    error_code = 10120
    msg = '参数错误'


########## Token相关(10200~10300) ##########
class TokenException(APIException):
    code = 401
    error_code = 10200
    msg = 'Token已过期或无效Token'


########## 文件相关(10300~10400) ##########
class FileTooLargeException(APIException):
    code = 413
    msg = '文件体积过大'
    error_code = 10310


class FileTooManyException(APIException):
    code = 413
    msg = '文件数量过多'
    error_code = 10320


class FileExtensionException(APIException):
    code = 401
    msg = '文件扩展名不符合规范'
    error_code = 10330


if __name__ == '__main__':
    server_error = ServerError()
    # server_error = ServerError(code=500, error_code=2000, msg='hello')
    print(server_error.get_description())
