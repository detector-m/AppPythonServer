#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :singleton.py
@说明        : Python与设计模式--单例模式 ->
https://developer.aliyun.com/article/70418
@时间        :2020/08/13 16:40:17
@作者        :Riven
@版本        :1.0.0
'''

import threading
import time

# 这里使用方法__new__来实现单例模式
# 抽象单列
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)

        return cls._instance

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