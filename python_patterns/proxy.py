#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :proxy.py
@说明        :代理模式 （Proxy）
https://www.cnblogs.com/taosiyu/p/11293949.html
https://www.cnblogs.com/onepiece-andy/p/python_proxy_pattern.html
http://www.pythontip.com/python-patterns/detail/proxy
https://developer.aliyun.com/article/70738
@时间        :2020/08/19 21:54:23
@作者        :Riven
@版本        :1.0.0
'''

'''
代理模式 （Proxy）
内容：为其他对象提供一种代理以控制对这个对象的访问。

角色：
抽象实体（Subject）
实体（RealSubject）
代理（Proxy）

适用场景：
远程代理：为远程的对象提供代理
虚代理：根据需要创建很大的对象
保护代理：控制对原始对象的访问，用于对象有不同访问权限时

优点：
远程代理：可以隐藏对象位于远程地址空间的事实
虚代理：可以进行优化，例如根据要求创建对象
保护代理：允许在访问一个对象时有一些附加的内务处理
'''

# # 方式一
# import time

# class SalesManager:
#     def work(self):
#         print('Sales Manager working...')

#     def talk(self):
#         print('Sales Manager ready to talk')

# class Proxy:
#     def __init__(self):
#         self.busy = 'No'
#         self.sales = None

#     def work(self):
#         print('Proxy checking for Sales Manager availability')
#         if self.busy == 'No':
#             self.sales = SalesManager()
#             time.sleep(2)
#             self.sales.talk()
#         else:
#             time.sleep(2)
#             print('Sales Manager is busy')

# if __name__ == '__main__':
#     p = Proxy()
#     p.work()
#     p.busy = 'Yes'
#     p.work()

# 方式二
from abc import ABCMeta, abstractclassmethod

class Subject(metaclass=ABCMeta):
    @abstractclassmethod
    def get_content(self):
        pass

    def set_content(self, content):
        pass

class RealSubject(Subject):
    def __init__(self, file_name):
        self.file_name = file_name
        print(f'读取{file_name}文件内容')
        f = open(file_name)
        self.__content = f.read()
        f.close()

    def get_content(self):
        return self.__content

    def set_content(self, content):
        f = open(self.file_name, 'w')
        f.write(content)
        self.__content = content
        f.close()

# 远程代理
class ProxyA(Subject):
    def __init__(self, file_name):
        self.subj = RealSubject(file_name)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        self.subj.set_content(content)

# 虚代理
class ProxyB(Subject):
    def __init__(self, file_name):
        self.file_name = file_name
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.file_name)
        
        return self.subj.get_content()

# 保护代理
class ProxyC(Subject):
    def __init__(self, file_name):
        self.subj = RealSubject(file_name)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError

if __name__ == '__main__':
    pa = ProxyA('README.md')
    # print('ProxyA')
    print(pa.subj)
    print(pa.get_content())

    pb = ProxyB('README.md')
    # print('ProxyB')
    print(pb.subj)
    print(pb.get_content())

    pc = ProxyC('README.md')
    # print('ProxyC')
    print(pc.subj)
    print(pc.get_content())

    
    