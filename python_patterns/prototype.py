#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :prototype.py
@说明        :原型模式（Prototype）
https://www.cnblogs.com/taosiyu/p/11293949.html#autoid-1-4-0
http://www.pythontip.com/python-patterns/detail/prototype
https://www.cnblogs.com/onepiece-andy/p/python_prototype_pattern.html
@时间        :2020/08/27 15:40:52
@作者        :Riven
@版本        :1.0.0
'''

'''
原型模式（Prototype）
内容：用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。

使用场景：
通过动态装载；
为了避免创建一个与产品类层次平行的工厂类层次时；
当一个类的实例只能有几个不同状态组合中的一种时。建立相应数目的原型并克隆它们可能比每次用合适的状态手工实例化该类更方便一些。
'''

# 方式1
import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        # Register an object
        self._objects[name] = obj

    def unregister_object(self, name):
        # Unregister an object
        del self._objects[name]

    def clone(self, name, **attr):
        # Clone a registered object and update inner attributes dictionary
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

def main():
    class TestA:
        def __str__(self):
            return 'I am TestA'

    a = TestA()
    prototype = Prototype()
    prototype.register_object('a', a)
    b = prototype.clone('a', a=1, b=2, c=3)
    c = prototype.clone('a', **{'a': 4, 'b': 5, 'c': 6})

    print(a)
    print(b.a, b.b, b.c)
    print(c.a, c.b, c.c)

    
if __name__ == '__main__':
    main()

# 方式2
# from abc import abstractclassmethod, ABCMeta
# import copy

# # 原型抽象类
# class Prototype(metaclass=ABCMeta):
#     @abstractclassmethod
#     def clone(self):
#         pass

#     @abstractclassmethod
#     def deep_clone(self):
#         pass

# # 工作经历
# class WorkExperience:
#     def __init__(self):
#         self.timearea = ''
#         self.company = ''

#     def set_workexperience(self, timearea, company):
#         self.timearea = timearea
#         self.company = company

# # 简历类
# class Resume(Prototype):
#     def __init__(self, name):
#         self.name = name
#         self.workexperience = WorkExperience()

#     def set_personinfo(self, sex, age):
#         self.sex = sex
#         self.age = age

#     def set_workexperience(self, timearea, company):
#         self.workexperience.set_workexperience(timearea, company)

#     def display(self):
#         print(self.name)
#         print(f'{self.sex}, {self.age}')
#         print(f'工作经历 {self.workexperience.timearea}, {self.workexperience.company}')

#     def clone(self):
#         return copy.copy(self)

#     def deep_clone(self):
#         return copy.deepcopy(self)

# if __name__ == "__main__":
#     obj1 = Resume('andy')
#     obj2 = obj1.clone()  # 浅拷贝对象
#     obj3 = obj1.deep_clone()  # 深拷贝对象

#     obj1.set_personinfo('男', 28)
#     obj1.set_workexperience('2010-2015', 'AA')
#     obj2.set_personinfo('女', 27)
#     obj2.set_workexperience('2011-2019', 'BB')  # 修改浅拷贝的对象工作经历
#     obj3.set_personinfo('男', 29)
#     obj3.set_workexperience('2016-2020', 'CC')  # 修改深拷贝的对象的工作经历
    
#     obj1.display()
#     obj2.display()
#     obj3.display()
