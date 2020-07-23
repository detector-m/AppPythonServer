#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :setting.py
@说明        :Flask 对配置项的限制，你必须保证命名全都大写，才能注入到current_app.config中
@时间        :2020/07/23 14:23:52
@作者        :Riven
@版本        :1.0.0
'''

# import os

ENV = 'development'
# DEBUG = True
SECRET_KEY = 'AppPythonServer'

# 在浏览器请求接口正常显示中文，而不是字节码
JSON_AS_ASCII = False

'''
应用于Swagger的URL，会自动添加协议前缀(http://或者https://)，因为会切换协议前缀
local_setting.py中 SERVER_URL = '127.0.0.1:8010'
'''
# SERVER_URL = '127.0.0.1:8010'  # 外部（云服务器）地址