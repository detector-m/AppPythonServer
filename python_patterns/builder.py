#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :builder.py
@说明        :建造者模式（Builder）
https://www.cnblogs.com/taosiyu/p/11293949.html
https://www.cnblogs.com/onepiece-andy/p/python-builder-pattern.html
https://developer.aliyun.com/article/70416
http://www.pythontip.com/python-patterns/detail/builder
@时间        :2020/08/18 22:14:47
@作者        :Riven
@版本        :1.0.0
'''

'''
建造者模式（Builder）
内容：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。

角色：
抽象建造者（Builder）
具体建造者（Concrete Builder）
指挥者（Director）
产品（Product）

建造者模式与抽象工厂模式相似，也用来创建复杂对象。主要区别是建造者模式着重一步步构造一个复杂对象，而抽象工厂模式着重于多个系列的产品对象。

适用场景：
当创建复杂对象的算法（Director）应该独立于该对象的组成部分以及它们的装配方式（Builder）时
当构造过程允许被构造的对象有不同的表示时（不同Builder）。

优点：
隐藏了一个产品的内部结构和装配过程
将构造代码与表示代码分开
可以对构造过程进行更精细的控制
'''

import abc

# 产品
class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s, %s, %s, %s" % (self.face, self.arm, self.body, self.leg)

# 建造者
# 抽象建造者
class Builder(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def build_face(self):
        pass

    @abc.abstractclassmethod
    def build_arm(self):
        pass

    @abc.abstractclassmethod
    def build_leg(self):
        pass

    @abc.abstractclassmethod
    def build_body(self):
        pass

# 具体建造者
class PlayerBuilder(Builder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = 'Face'
    
    def build_arm(self):
        self.player.arm = 'Arm'

    def build_leg(self):
        self.player.leg = 'Leg'

    def build_body(self):
        self.player.body = 'Body'

    def get_player(self):
        return self.player
    
# 指挥者
class Director:
    def build_player(self, builder):
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        builder.build_body()

        return builder.get_player()


if __name__ == "__main__":
    director = Director()
    builder = PlayerBuilder()
    player = director.build_player(builder)
    print(player)
