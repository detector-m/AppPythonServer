#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :data_adapter.py
@说明        :适配器模式: http://www.pythontip.com/python-patterns/detail/adapter
@时间        :2020/07/29 14:11:37
@作者        :Riven
@版本        :1.0.0
'''

import sys
sys.path.append('.')
from app_server.src.data.data_interface import DataInterface

class DataM1(DataInterface):
    def save(self, save_data, path=None):
        print(self.__class__.__name__ + ' ' + self.save.__name__)

        if not path or not save_data:
            return None
                
    def fetch(self, fetch_data=None, path=None):
        print(self.__class__.__name__ + ' ' + self.fetch.__name__)

        if not path:
            return None

class DataM2(DataInterface):
    def save(self, save_data, path=None):
        print(self.__class__.__name__ + ' ' + self.save.__name__)

        if not path or not save_data:
            return None
                
    def fetch(self, fetch_data=None, path=None):
        print(self.__class__.__name__ + ' ' + self.fetch.__name__)

        if not path:
            return None

class DataAdapter(object):
    def __init__(self, data_interface: DataInterface, *, adapted_methods=None):
        """We set the adapted methods in the object's dict"""
        self.data_interface = data_interface
        if adapted_methods is not None:
            self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.data_interface, attr)

if __name__ == '__main__':
    data_m1 = DataM1()
    adapter1 = DataAdapter(data_m1, adapted_methods=dict(test=data_m1.save))
    adapter1.test({})

    data_m2 = DataM2()
    adapter2 = DataAdapter(data_m2)
    adapter2.save({})