#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :account_manager.py
@说明        :
@时间        :2020/07/24 23:03:27
@作者        :Riven
@版本        :1.0.0
'''

import plistlib
import os, sys

if __name__ == '__main__':
    path = os.getcwd() + '/app_server/data/account_list.plist'

    with open(path, 'rb') as fp:
        try:
            ret_dict = plistlib.load(fp)
        # except:
            # print(sys.exc_info())
        except plistlib.InvalidFileException as e:
            ret_dict = {}
        # except e: Exception:
        #     print(e)
        #     ret_dict = {}
        #     return
            

        print(ret_dict)


    with open(path, 'wb') as fp:
        a_dict_1 = {
            'name': '15012341234',
            'phone': '15012341234',
            'password': '123456'
        }

        a_dict_2 = {
            'name': '15012345678',
            'phone': '15012341234',
            'password': '654321'
        }
        ret_dict = {}
        ret_dict['account_list'] = [a_dict_1, a_dict_2]
        plistlib.dump(ret_dict, fp)
