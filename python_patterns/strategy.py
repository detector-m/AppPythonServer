#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :strategy.py
@说明        :策略模式（Strategy）
https://www.cnblogs.com/taosiyu/p/11293949.html
http://www.pythontip.com/python-patterns/detail/strategy
https://www.cnblogs.com/onepiece-andy/p/python-strategy.html
https://developer.aliyun.com/article/71071
@时间        :2020/08/17 22:48:16
@作者        :Riven
@版本        :1.0.0
'''

'''
策略模式（Strategy）
内容：定义一系列的算法，把它们一个个封装起来，并且使它们可相互替换。本模式使得算法可独立于使用它的客户而变化。

角色：
抽象策略（Strategy）
具体策略（ConcreteStrategy）
上下文（Context）

适用场景：
许多相关的类仅仅是行为有异
需要使用一个算法的不同变体
算法使用了客户端无需知道的数据
一个类中的多种行为以多个条件语句的形式存在，可以将这些行为封装如不同的策略类中。

优点：
定义了一系列可重用的算法和行为
消除了一些条件语句
可以提供相同行为的不同实现

缺点：
客户必须了解不同的策略
策略与上下文之间的通信开销
增加了对象的数目
'''

# 方式一
# import types

# class StrategyExample:
#     def __init__(self, func=None):
#         self.name = 'Strategy Example 0'
#         if func is not None:
#             self.execute = types.MethodType(func, self)

#     def execute(self):
#         print(self.name)

# def execute_replacement1(self):
#     print(self.name + 'from execute 1')

# def execute_replacement2(self):
#     print(self.name + 'from execute 2')

# if __name__ == '__main__':
#     strat0 = StrategyExample()
 
#     strat1 = StrategyExample(execute_replacement1)
#     strat1.name = 'Stragety 1'

#     strat2 = StrategyExample(execute_replacement2)
#     strat2.name = 'Strategy 2'

#     strat0.execute()
#     strat1.execute()
#     strat2.execute()

# 方式二
from abc import ABCMeta, abstractclassmethod
import random

class Sort(metaclass=ABCMeta):
    @abstractclassmethod
    def sort(self, data):
        pass

class QuickSort(Sort):
    def quick_sort(self, data, left, right):
        if left < right:
            mid = self.partition(data, left, right)
            self.quick_sort(data, left, mid-1)
            self.quick_sort(data, mid+1, right)

    def partition(self, data, left, right):
        tmp = data[left]
        while left < right:
            while left < right and data[right] >= tmp:
                right -= 1
            data[left] = data[right]

            while left < right and data[left] <= tmp:
                left += 1
            data[right] = data[left]

        data[left] = tmp

        return left


    def sort(self, data):
        print('快速排序')
        return self.quick_sort(data, 0, len(data)-1)

class MergeSort(Sort):
    def merge_sort(self, data, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(data, low, mid)
            self.merge_sort(data, mid+1, high)
            self.merge(data, low, mid, high)

    def merge(self, data, low, mid, high):
        i = low
        j = mid + 1
        ltmp = []

        while i<=mid and j<=high:
            if data[i] <= data[j]:
                ltmp.append(data[i])
                i += 1
            else:
                ltmp.append(data[j])
                j += 1
        
        while i<=mid:
            ltmp.append(data[i])
            i += 1

        while j<=high:
            ltmp.append(data[j])
            j += 1

        data[low: high+1] = ltmp

    def sort(self, data):
        print('归并排序')
        return self.merge_sort(data, 0, len(data)-1)

class Context:
    def __init__(self, data, strategy=None):
        self.data = data
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        if self.strategy:
            self.strategy.sort(self.data)
        else:
            raise TypeError

    

if __name__ == '__main__':
    li = list(range(10000))
    random.shuffle(li)

    context = Context(li, MergeSort())
    context.do_strategy()

    random.shuffle(context.data)

    context.set_strategy(QuickSort())
    context.do_strategy()

