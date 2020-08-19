#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :decorator.py
@说明        :装饰器模式 (Decorator)
https://www.cnblogs.com/onepiece-andy/p/python-decorator-pattern.html
https://www.cnblogs.com/welan/p/9127542.html
http://www.pythontip.com/python-patterns/detail/decorator
https://www.jianshu.com/p/013985a58841
@时间        :2020/08/19 11:47:16
@作者        :Riven
@版本        :1.0.0
'''

'''
装饰模式(Decorator Pattern)
内容：动态地给一个对象增加一些额外的职责。就扩展功能而言，装饰模式提供了一种比使用子类更加灵活的替代方案。以对客户透明的方式动态地给一个对象附加上更多的责任 可以在不需要创建更多子类的情况下，让对象的功能得以扩展

角色：
Component（抽象构件）
ConcreteComponent（具体构件）
Decorator（抽象装饰类）
ConcreteDecorator（具体装饰类）

优点：
对于扩展一个对象的功能，装饰模式比继承更加灵活，不会导致类的个数急剧增加 可以通过一种动态的方式来扩展一个对象的功能，通过配置文件可以在运行时选择不同的具体装饰类，从而实现不同的行为 可以对一个对象进行多次装饰 具体构件类与具体装饰类可以独立变化，用户可以根据需要增加新的具体构件类和具体装饰类，且原有类库代码无须改变，符合开闭原则

缺点：
使用装饰模式进行系统设计时将产生很多小对象，大量小对象的产生势必会占用更多的系统资源，在一定程度上影响程序的性能 比继承更加易于出错，排错也更困难，对于多次装饰的对象，调试时寻找错误可能需要逐级排查，较为烦琐

适用性：
在不影响其他对象的情况下，以动态、透明的方式给单个对象添加职责。
处理那些可以撤消的职责。
'''
# 方式一
from abc import ABCMeta, abstractclassmethod

# 定义对象接口
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'装扮的{self.name}')

# 装饰类
class Decorator(metaclass=ABCMeta):
    def decorate(self, componet):
        self.componet = componet

    @abstractclassmethod
    def show(self):
        pass

# 装扮——T恤
class TShirts(Decorator):
    def show(self):
        print("T恤")
        self.componet.show()


# 装扮——大裤衩
class Trouser(Decorator):
    def show(self):
        print("大裤衩")
        self.componet.show()


if __name__ == '__main__':
    p = Person('Riven')
    ts = TShirts()
    tr = Trouser()

    ts.decorate(p)
    tr.decorate(ts)
    tr.show()

# # 方式二
# class Foo:
#     def f1(self):
#         print('f1')

#     def f2(self):
#         print('f2')

# class Decorator:
#     def __init__(self, decoratee):
#         self._decoratee = decoratee

#     def f1(self):
#         print('decorated f1')
#         self._decoratee.f1()

#     def __getattr__(self, name):
#         return getattr(self._decoratee, name)

# if __name__ == '__main__':
#     foo = Foo()
#     decorator = Decorator(foo)
#     decorator.f1()
#     decorator.f2()