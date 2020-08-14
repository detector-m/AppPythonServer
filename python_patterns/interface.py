#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :interface.py
@说明        : 接口 -> 浅谈设计模式及python实现
https://www.cnblogs.com/taosiyu/p/11293949.html
@时间        :2020/08/14 14:44:07
@作者        :Riven
@版本        :1.0.0
'''

'''
设计模式六大原则

1. 开闭原则：一个软件实体如类、模块和函数应该对扩展开放，对修改关闭。即软件实体应尽量在不修改原有代码的情况下进行扩展。
2. 里氏（Liskov）替换原则：所有引用基类（父类）的地方必须能透明地使用其子类的对象。
3. 依赖倒置原则：高层模块不应该依赖低层模块，二者都应该依赖其抽象；抽象不应该依赖细节；细节应该依赖抽象。换言之，要针对接口编程，而不是针对实现编程。
4. 接口隔离原则：使用多个专门的接口，而不使用单一的总接口，即客户端不应该依赖那些它不需要的接口。
5. 迪米特法则：一个软件实体应当尽可能少地与其他实体发生相互作用。
6. 单一职责原则：不要存在多于一个导致类变更的原因。通俗的说，即一个类只负责一项职责。
'''

'''
接口

接口：一种特殊的类，声明了若干方法，要求继承该接口的类必须实现这些方法。
作用：限制继承接口的类的方法的名称及调用方式；隐藏了类的内部实现。

接口就是一种抽象的基类（父类），限制继承它的类必须实现接口中定义的某些方法。

Python中使用ABCMeta、abstractmethod的抽象类、抽象方法来实现接口的功能。接口类定义方法，不具体实现，限制子类必须有该方法。在接口子类中实现具体的功能。
'''

# 通过抽象类和抽象方法，抽象出基类 -> 接口
from abc import ABCMeta
# 导入抽象方法
from abc import abstractclassmethod 

# 创建抽象类
class Interface(metaclass=ABCMeta):
    @abstractclassmethod
    def func1(self):
        pass

    @abstractclassmethod
    def func2(self):
        pass

if __name__ == '__main__':

    # 具体类
    class Test(Interface):
        def func1(self):
            print('Test.func1')

        def func2(self):
            print('func2')

    obj = Test()
    obj.func1()
