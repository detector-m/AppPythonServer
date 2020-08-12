#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :abstract_factory.py
@说明        : 抽象工厂模式-> 抽象工厂模式(Abstract Factory Pattern):提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们的类
http://www.pythontip.com/python-patterns/detail/abstract_factory
https://www.cnblogs.com/onepiece-andy/p/python-abstract-factory-pattern.html
@时间        :2020/08/10 22:40:22
@作者        :Riven
@版本        :1.0.0
'''

__author__ = 'Riven'

import abc

# 抽象用户表类(接口)
class User(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get_user(self):
        pass

    @abc.abstractclassmethod
    def insert_user(self):
        pass

# 抽象部门表类（接口）
class Departemnt(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get_department(self):
        pass

    @abc.abstractclassmethod
    def insert_department(self):
        pass

# 抽象工厂类 （接口）
class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def create_user(self):
        pass

    @abc.abstractclassmethod
    def create_departent(self):
        pass

# 具体用户表类-Mysql
class MysqlUser(User):
    def get_user(self):
        print('MysqlUser get User')

    def insert_user(self):
        print('MysqlUser insert User')

# 具体部门表类-Mysql
class MysqlDepartment(Departemnt):
    def get_department(self):
        print('MysqlDepartment get department')
    
    def insert_department(self):
        print('MysqlDepartment insert department')

# 具体工厂类-Mysql
class MysqlFactory(AbstractFactory):
    def create_user(self):
        return MysqlUser()

    def create_departent(self):
        return MysqlDepartment()

# 具体用户表类-Orcale
class OrcaleUser(User):
    def get_user(self):
        print('OrcaleUser get User')

    def insert_user(self):
        print('OrcaleUser insert User')

# 具体部门表类-OrcaleUser
class OrcaleDepartment(Departemnt):
    def get_department(self):
        print('OrcaleDepartment get department')
    
    def insert_department(self):
        print('OrcaleDepartment insert department')

# 具体工厂类-Orcale
class OrcaleFactory(AbstractFactory):
    def create_user(self):
        return OrcaleUser()

    def create_departent(self):
        return OrcaleDepartment()

if __name__ == '__main__':
    # db = 'Mysql'
    db = 'Orcale'

    if db == 'Mysql':
        my_factory = MysqlFactory()
    elif db == 'Orcale':
        my_factory = OrcaleFactory()
    else:
        print('无法识别的类型')
        exit(0)

    user = my_factory.create_user()
    department = my_factory.create_departent()

    user.insert_user()
    user.get_user()
    department.insert_department()
    department.get_department()
