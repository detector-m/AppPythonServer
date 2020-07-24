#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :api_login.py
@说明        :
@时间        :2020/07/24 10:53:35
@作者        :Riven
@版本        :1.0.0
'''

from flask import Blueprint

api_login_module = Blueprint('api_login_module', __name__)

@api_login_module.route('/login')
def login():
    return '用户登录'

@api_login_module.route('/register')
def register():
    return '用户注册'