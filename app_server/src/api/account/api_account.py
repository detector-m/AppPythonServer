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

api_account_module = Blueprint('api_account_module', __name__)

@api_account_module.route('/login')
def login():
    return '用户登录'

@api_account_module.route('/register', methods=['POST', 'GET'])
def register():
    # if (request.method == 'POST'):
    #     req_form_dict = request.form.to_dict()
    # else:
    #     req_args_dict = request.args.to_dict()

    req_args_dict = request.args.to_dict()
    req_form_dict = request.form.to_dict()

    print(req_args_dict)
    print(req_form_dict)

    return '用户注册'