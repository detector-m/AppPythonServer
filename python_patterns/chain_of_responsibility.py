#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :chain_of_responsibility.py
@说明        :责任链模式（Chain of Responsibility）
https://www.cnblogs.com/taosiyu/p/11293949.html#autoid-1-4-0
https://www.cnblogs.com/onepiece-andy/p/python-chain-of-responsibility.html
http://www.pythontip.com/python-patterns/detail/chain
@时间        :2020/09/01 15:24:03
@作者        :Riven
@版本        :1.0.0
'''

'''
责任链模式（Chain of Responsibility）
内容：使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。

角色：
抽象处理者（Handler）
具体处理者（ConcreteHandler）
客户端（Client）

例：
请假部门批准：leader—>部门经理—>总经理
Javascript事件浮升机制

适用场景：
有多个对象可以处理一个请求，哪个对象处理由运行时决定
在不明确接收者的情况下，向多个对象中的一个提交一个请求

优点：
降低耦合度：一个对象无需知道是其他哪一个对象处理其请求

缺点：
请求不保证被接收：链的末端没有处理或链配置错误
'''

from abc import ABCMeta, abstractclassmethod

# 抽象一个处理类
class Handler(metaclass=ABCMeta):
    def set_successor(self, successor):
        self.successor = successor

    @abstractclassmethod
    def handle_request(self, request):
        pass

# 具体的处理中类1
class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request < 10:
            print(f'总经理批准{request}天假')
        else:
            print('请假天数过长')
            # self.successor.handle_request(request)

# 具体的处理中类2
class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request < 7:
            print(f'部门经理批准{request}天假')
        else:
            self.successor.handle_request(request)

# 具体的处理中类3
class ConcreteHandler3(Handler):
    def handle_request(self, request):
        if request < 3:
            print(f'项目主管批准{request}天假')
        else:
            self.successor.handle_request(request)


if __name__ == '__main__':
    ch1 = ConcreteHandler1()
    ch2 = ConcreteHandler2()
    ch3 = ConcreteHandler3()

    ch3.set_successor(ch2)
    ch2.set_successor(ch1)

    ch3.handle_request(20)