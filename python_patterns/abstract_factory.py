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

'''
抽象工厂方法（Abstract Factory）
定义一个工厂类接口，让工厂子类来创建一系列相关或相互依赖的对象。

角色：
抽象工厂角色（Creator）
具体工厂角色（Concrete Creator）
抽象产品角色（Product）
具体产品角色（Concrete Product）
客户端（Client）

相比工厂方法模式，抽象工厂模式中的每个具体工厂都生产一套产品。

适用场景：
系统要独立于产品的创建与组合时
强调一系列相关的产品对象的设计以便进行联合使用时
提供一个产品类库，想隐藏产品的具体实现时

优点：
将客户端与类的具体实现相分离
每个工厂创建了一个完整的产品系列，使得易于交换产品系列
有利于产品的一致性（即产品之间的约束关系）

缺点：
难以支持新种类的（抽象）产品
'''

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
