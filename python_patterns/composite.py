#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :composite.py
@说明        :组合模式（Composite）
https://www.cnblogs.com/taosiyu/p/11293949.html#autoid-1-4-0
http://www.pythontip.com/python-patterns/detail/composite
https://www.cnblogs.com/onepiece-andy/p/python-composite-pattern.html
@时间        :2020/08/31 09:43:11
@作者        :Riven
@版本        :1.0.0
'''

'''
组合模式（Composite）
内容：将对象组合成树形结构以表示“部分-整体”的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性。

角色：
抽象组件（Component）
叶子组件（Leaf）
复合组件（Composite）
客户端（Client）

适用场景：
表示对象的“部分-整体”层次结构（特别是结构是递归的）
希望用户忽略组合对象与单个对象的不同，用户统一地使用组合结构中的所有对象

优点：
定义了包含基本对象和组合对象的类层次结构
简化客户端代码，即客户端可以一致地使用组合对象和单个对象
更容易增加新类型的组件

缺点：
很难限制组合中的组件
'''

from abc import abstractclassmethod, ABCMeta

# 抽象一个组件类
class Component(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def add(self, comp):
        pass

    @abstractclassmethod
    def remove(self, comp):
        pass

    @abstractclassmethod
    def display(self, depth):
        pass

# 叶子节点
class Leaf(Component):
    def add(self, comp):
        print('不能添加下级节点')

    def remove(self, comp):
        print('不能删除下级节点')

    def display(self, depth):
        strtemp = ''

        for i in range(depth):
            strtemp += strtemp+'-'

        print(strtemp+self.name)

# 复合组件
class Composite(Component):

    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, comp):
        self.children.append(comp)

    def remove(self, comp):
        self.children.remove(comp)

    def display(self, depth):
        strtemp = ''

        for i in range(depth):
            strtemp += strtemp+'-'

        print(strtemp+self.name)

        for comp in self.children:
            comp.display(depth+2)

if __name__ == '__main__':
    # 生成根
    root = Composite('root')
    # 叶子节点
    root.add(Leaf('leaf A'))
    root.add(Leaf('leaf B'))

    # 分支
    comp = Composite('composite X')
    comp.add(Leaf('leaf XA'))
    comp.add(Leaf('leaf XB'))
    root.add(comp)

    comp = Composite('composite Y')
    comp.add(Leaf('leaf YA'))
    root.add(comp)

    root.display(1)