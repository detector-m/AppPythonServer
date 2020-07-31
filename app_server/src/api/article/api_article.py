#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :api_article.py
@说明        :
@时间        :2020/07/31 22:17:26
@作者        :Riven
@版本        :1.0.0
'''

from flask import Blueprint, request

import sys
sys.path.append('.')
from app_server.src.error import error

api_article_module = Blueprint('api_article_module', __name__)

@api_article_module.route('/article_list', methods=['GET', 'POST'])
def article_list():
    data = {
        'id': '1', 
        'name': '好', 
        'content': '12345678900987654321'
    }
    return error.Success(data=data)
