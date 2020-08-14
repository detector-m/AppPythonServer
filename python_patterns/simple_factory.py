#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :simple_factory.py
@说明        :简单工厂模式 ->
https://www.cnblogs.com/taosiyu/p/11293949.html
@时间        :2020/08/14 14:59:46
@作者        :Riven
@版本        :1.0.0
'''

'''
简单工厂模式：
不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例。

角色：
工厂角色（Creator）
抽象产品角色（Product）
具体产品角色（Concrete Product）

优点：
隐藏了对象创建的实现细节
客户端不需要修改代码

缺点：
违反了单一职责原则，将创建逻辑几种到一个工厂类里
当添加新产品时，需要修改工厂类代码，违反了开闭原则
'''

import abc

class Payment(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def __init__(self, enable_yuebao=False):
        self.enable_yuebao = enable_yuebao

    def pay(self, money):
        if self.enable_yuebao:
            print(f'余额宝支付{money}元')
        else:
            print(f'支付宝支付{money}元')

class WeChatPay(Payment):
    def pay(self, money):
        print(f'微信支付{money}元')

class PaymentFactory:
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'yuebao':
            return Alipay(enable_yuebao=True)
        elif method == 'wechatpay':
            return WeChatPay()
        else:
            raise NameError(method)

if __name__ == '__main__':
    f = PaymentFactory()
    p = f.create_payment('alipay')
    p.pay(1000000)