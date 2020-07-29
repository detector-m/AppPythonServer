#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :data_interface.py
@说明        :数据接口
@时间        :2020/07/29 14:13:14
@作者        :Riven
@版本        :1.0.0
'''

import abc

'''
定义一个接口
'''
class DataInterface(metaclass=abc.ABCMeta):
    # For Test
    # path = ' 123543'
    # def __init__(self):
        # self.path = '123'

    @abc.abstractclassmethod
    def save(self, data, path):
        # raise NotImplementedError
        pass

    @abc.abstractclassmethod
    def fetch(self, path):
        # raise NotImplementedError
        pass