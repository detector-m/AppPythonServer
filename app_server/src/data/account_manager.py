#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :account_manager.py
@说明        :
@时间        :2020/07/24 23:03:27
@作者        :Riven
@版本        :1.0.0
'''
import os

import sys
sys.path.append('.')
from app_server.src.data.data_interface import DataInterface
from app_server.src.data.data_adapter import DataAdapter

class AccountDataInterface(DataInterface):
    def save(self, data, path):
        print(type(AccountDataInterface))
        # print('DataM1, save' + DataInterface.path)
        print('DataM1, save')
        print(self.__class__.__name__ + ' ' + self.save.__class__.__name__)
        print(type(self.save))

    def fetch(self, path):
        print('DataM1, fetch')

class DataM1(AccountDataInterface):
    pass

class DataM2(AccountDataInterface):
    pass

class AccountManager(DataAdapter):
    def __init__(self, data_interface: DataInterface, *, path=None):
        # super().__init__(data_interface)
        DataAdapter.__init__(self, data_interface)

        if not path:
            self.path = os.getcwd() + '/app_server/data/account_list.plist'
        else:
            self.path = path
    

if __name__ == '__main__':
    data_m1 = DataM1()
    adapter1 = AccountManager(data_m1)
    adapter1.save({}, 'a')

    data_m2 = DataM2()
    adapter2 = AccountManager(data_m2)
    adapter2.save({}, 'a')