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
from app_server.src.api.login.api_login import api_login_module

def home():
    data = 'this is home'
    return data

def init_routes(app: Flask):
    app.add_url_rule('/', 'home', home)

    @app.route('/api')
    @app.route('/api/api_login')
    def api_index():
        return 'api'

    @app.route('/test')
    def test():
        return 'Test'

    # 登录注册api 蓝图注册
    app.register_blueprint(api_login_module, url_prefix='/api/api_login')

    # app.add_url_rule('/extract/', 'extract', extract)
    # app.add_url_rule('/allow/', 'allow', allow)
    # app.add_url_rule('/desc/', 'desc', desc)