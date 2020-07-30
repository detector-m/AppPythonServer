#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :route.py
@说明        :
@时间        :2020/07/24 10:26:03
@作者        :Riven
@版本        :1.0.0
'''

from flask import Flask

import sys
sys.path.append('.')
from app_server.src.api.account.api_account import api_account_module
from app_server.src.api.api_constant import API_ROOT_PATH, API_ACCOUNT_ROOT_PATH
from app_server.src.error import error


ROOT_PATH = '/'

def home():
    data = 'this is home'
    return data

def init_routes(app: Flask):
    app.add_url_rule(ROOT_PATH, 'home', home)

    @app.route(ROOT_PATH+API_ROOT_PATH)
    @app.route(ROOT_PATH+API_ACCOUNT_ROOT_PATH)
    def api_index():
        return 'api'

    @app.route('/test')
    def test():
        success = error.Success(data={'google': 'hello'})
        return success.get_body()

    # 登录注册api 蓝图注册
    app.register_blueprint(api_account_module, url_prefix=ROOT_PATH+API_ACCOUNT_ROOT_PATH)

    # app.add_url_rule('/extract/', 'extract', extract)
    # app.add_url_rule('/allow/', 'allow', allow)
    # app.add_url_rule('/desc/', 'desc', desc)