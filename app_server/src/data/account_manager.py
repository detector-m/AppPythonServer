#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :account_manager.py
@说明        :
@时间        :2020/07/24 23:03:27
@作者        :Riven
@版本        :1.0.0
'''

import os, sys

sys.path.append('.')
from app_server.src.utils import plist_utils

class AccountManager(object):
    def __init__(self, path=None):
        # object.__init__(self)
        super().__init__()
        if not path:
            self.path = os.getcwd() + '/app_server/data/account_list.plist'
        else:
            self.path = path
        
        self.accounts_dict = self._get_accounts_dict()
        self.accounts = self.get_accounts()

    def get_account_with_phone(self, phone: str) -> dict:
        if not phone:
            return None

        for e_a in self.accounts:
            if e_a['phone'] == phone:
                return e_a
            
        return None

    def exist_account_with_phone(self, phone: str) -> bool:
        if not phone:
            return False
        
        for e_a in self.accounts:
            if e_a['phone'] == phone:
                return True
            
        return False

    def exist_account(self, a: dict) -> bool:
        for e_account in self.accounts:
            if (e_account['phone'] == a['phone']):
                return True
        
        return False

    def add_account(self, a: dict):
        if self.exist_account(a):
            return
        
        self.accounts.append(a)
        self.set_accounts(self.accounts)

    def remove_account(self, a: dict):
        for e_a in self.accounts:
            if (e_a['phone'] == a['phone']):
                self.accounts.pop(e_a)
                return

    def get_accounts(self):
        accounts = []
        if 'accounts' in self.accounts_dict.keys():
            accounts = self.accounts_dict['accounts']

        return accounts

    def set_accounts(self, accounts: list):
        self.accounts_dict['accounts'] = accounts
        self._set_accounts_dict()

    def _get_accounts_dict(self):
        ret_dict = plist_utils.read_content(self.path)

        return ret_dict

    def _set_accounts_dict(self):
        plist_utils.write_content(self.path, self.accounts_dict)
    
        

if __name__ == '__main__':
    manager = AccountManager()
    accounts = manager.get_accounts()
    
    a_dict_1 = {
            'name': '15012341234',
            'phone': '15012341234',
            'password': '123456'
        }
    accounts.append(a_dict_1)
    accounts.append(a_dict_1)
    manager.set_accounts(accounts)

    # path = os.getcwd() + '/app_server/data/account_list.plist'
    # with open(path, 'rb') as fp:
    #     try:
    #         ret_dict = plistlib.load(fp)
    #     # except:
    #         # print(sys.exc_info())
    #     except plistlib.InvalidFileException as e:
    #         ret_dict = {}
    #     # except e: Exception:
    #     #     print(e)
    #     #     ret_dict = {}
    #     #     return
            

        # print(ret_dict)

    # with open(path, 'wb') as fp:
        # a_dict_1 = {
        #     'name': '15012341234',
        #     'phone': '15012341234',
        #     'password': '123456'
        # }

    #     a_dict_2 = {
    #         'name': '15012345678',
    #         'phone': '15012341234',
    #         'password': '654321'
    #     }
    #     ret_dict = {}
    #     ret_dict['account_list'] = [a_dict_1, a_dict_2]
    #     plistlib.dump(ret_dict, fp)
