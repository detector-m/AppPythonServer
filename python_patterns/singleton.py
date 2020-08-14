#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :singleton.py
@说明        : Python与设计模式--单例模式 ->
https://zhuanlan.zhihu.com/p/31675841
https://developer.aliyun.com/article/70418
https://www.cnblogs.com/onepiece-andy/p/python-singleton-pattern.html
@时间        :2020/08/13 16:40:17
@作者        :Riven
@版本        :1.0.0
'''

import threading
import time

# 这里使用方法__new__来实现单例模式
# 抽象单列
# 方式1：带有属性的 
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)

        return cls._instance

# 方式2：利用__dict__来引用同一个字典
# class Singleton(object):
#     _state = {}
#     def __new__(cls, *args, **kwargs):
#         # ob = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         ob = super().__new__(cls, *args, **kwargs)
#         ob.__dict__ = cls._state

#         return ob

# 方式3: 利用元类在创建方法时用__metaclass__来创建
# class Singleton(type):
#     def __new__(cls, name, bases, dct):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls, name, bases, dct)
#             return cls._instance

# 方法3时
# 总线
# class Bus(metaclass=Singleton):
#     # def __new__(cls, *args, **kw):
#     #     if not hasattr(cls, '_instance'):
#     #         orig = super(Bus, cls)
#     #         # _instance = orig.__new__(cls, *args, **kw)
#     #         # if hasattr(cls, '_instance'):
#     #         #     print('has _instance')
#     #         # return _instance

#     #         return orig.__new__(cls, *args, **kw)

#     #     return cls._instance

#     # def __init__(self):
#     #     super(Bus, self).__init__()
#     #     print('init')

#     lock = threading.RLock()

#     def sendData(self, data):
#         self.lock.acquire()
#         time.sleep(3)
#         print('Sending Signal Data...' + data)
#         self.lock.release()

# 方式4: 利用装饰器
# def Singleton(cls, *args, **kwargs):
#     instance = {}
#     def _single():
#         if cls not in instance:
#             instance[cls] = cls(*args, **kwargs)
        
#         return instance[cls]

#     return _single

# # 方法4时
# # 总线
# @Singleton
# class Bus(object):
#     lock = threading.RLock()

#     def sendData(self, data):
#         self.lock.acquire()
#         time.sleep(3)
#         print('Sending Signal Data...' + data)
#         self.lock.release()

# 总线
class Bus(Singleton):
    # def __new__(cls, *args, **kw):
    #     if not hasattr(cls, '_instance'):
    #         orig = super(Bus, cls)
    #         # _instance = orig.__new__(cls, *args, **kw)
    #         # if hasattr(cls, '_instance'):
    #         #     print('has _instance')
    #         # return _instance

    #         return orig.__new__(cls, *args, **kw)

    #     return cls._instance

    # def __init__(self):
    #     super(Bus, self).__init__()
    #     print('init')

    lock = threading.RLock()

    def sendData(self, data):
        self.lock.acquire()
        time.sleep(3)
        print('Sending Signal Data...' + data)
        self.lock.release()

# 线程抽象，为更加说明单列的含义， 这里将Bus对象实例化写在run里
class VisitEntity(threading.Thread):
    my_bus = ''
    name = 'sss'

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):
        # print(VisitEntity.name)
        # print()
        self.my_bus = Bus()
        self.my_bus.sendData(self.name)

if __name__ == '__main__':
    # s = Singleton()
    # b = Bus()
    # b.sendData('hello')

    for i in range(3):
        print(f"Entity {i} begin to run...")
        my_entity = VisitEntity()
        my_entity.setName('Entity_'+str(i))
        my_entity.start()