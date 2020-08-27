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