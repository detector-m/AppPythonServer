#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :api_account.py
@说明        :
@时间        :2020/07/24 15:27:09
@作者        :Riven
@版本        :1.0.0
'''


from flask import Blueprint, request

import sys
sys.path.append('.')
from app_server.src.data import account_manager
from app_server.src.error import error

api_account_module = Blueprint('api_account_module', __name__)

@api_account_module.route('/login', methods=['POST'])
def login():
    req_form_dict = request.form.to_dict()
    if not req_form_dict:
        return error.ParameterException()

    try:
        account = {}
        account['phone'] = req_form_dict['phone']
        account['password'] = req_form_dict['password']
    except KeyError as e:
        return error.ParameterException()

    a_manager = account_manager.AccountManager()
    if not a_manager.exist_account(account):
        return error.NotFound(msg='用户不存在')
    
    exist_account = a_manager.get_account_with_phone(account['phone'])
    if account['password'] != exist_account['password']:
        return error.Failed(msg='账号/密码错误')

    res_dict = {'token': '12343212343234323445323'}

    return error.Success(msg='登录成功', data=res_dict)

# @api_account_module.route('/register', methods=['POST', 'GET'])
@api_account_module.route('/register', methods=['POST'])
def register():
    # if (request.method == 'POST'):
    #     req_form_dict = request.form.to_dict()
    # else:
    #     req_args_dict = request.args.to_dict()

    req_form_dict = request.form.to_dict()
    if not req_form_dict:
        return error.ParameterException()
    
    try:
        account = {}
        account['phone'] = req_form_dict['phone']
        account['password'] = req_form_dict['password']
    except KeyError as e:
        return error.ParameterException()

    a_manager = account_manager.AccountManager()
    if a_manager.exist_account(account):
        return error.RepeatException(msg='已注册')

    a_manager.add_account(account)

    return error.Success(error_code=1, msg='注册成功')