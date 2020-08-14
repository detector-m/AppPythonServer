#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :factory_method.py
@说明        :工厂方法模式（Factory Method）
https://www.cnblogs.com/taosiyu/p/11293949.html

@时间        :2020/08/14 22:33:15
@作者        :Riven
@版本        :1.0.0
'''

'''
工厂方法模式（Factory Method）：
定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类。

角色：
抽象工厂角色（Creator）
具体工厂角色（Concrete Creator）
抽象产品角色（Product）
具体产品角色（Concrete Product）

工厂方法模式相比简单工厂模式将每个具体产品都对应了一个具体工厂。

适用场景：
需要生产多种、大量复杂对象的时候。
需要降低耦合度的时候。
当系统中的产品种类需要经常扩展的时候。

优点：
每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
隐藏了对象创建的实现细节

缺点：
每增加一个具体产品类，就必须增加一个相应的具体工厂类
'''

from abc import abstractclassmethod, ABCMeta

class Payment(metaclass=ABCMeta):
    @abstractclassmethod
    def pay(self, money):
        pass
    
class Alipay(Payment):
    def pay(self, money):
        print(f'支付宝支付{money}元')

class WeChatPay(Payment):
    def pay(self, money):
        print(f'微信支付{money}元')

class PaymentFactory(metaclass=ABCMeta):
    @abstractclassmethod
    def create_payment(self):
        pass

class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

class WeChatPayFactory(PaymentFactory):
    def create_payment(self):
        return WeChatPay()

if __name__ == '__main__':
    af = AlipayFactory()
    ali = af.create_payment()
    ali.pay(120)

    wf = WeChatPayFactory()
    wchat = wf.create_payment()
    wchat.pay(100)

