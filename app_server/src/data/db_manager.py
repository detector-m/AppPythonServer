#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :db_manager.py
@说明        :
在python中，使用sqlite3创建数据库的连接，当我们指定的数据库文件不存在的时候连接对象会自动创建数据库文件；如果数据库文件已经存在，则连接对象不会再创建数据库文件，而是直接打开该数据库文件。连接对象可以是硬盘上面的数据库文件，也可以是建立在内存（memory）中的，在内存中的数据库执行完任何操作后，都不需要提交事务的(commit)

  connect方法返回con对象，即是数据库链接对象，它提供了以下方法：

    方法	    描述
.cursor()	创建一个游标对象
.commit()	处理事务提交
.rollback()	处理事务回滚
.close()	关闭一个数据库连接

参考使用方式：https://blog.csdn.net/GuoQiZhang/article/details/91344509

异步sqlite框架：https://github.com/omnilib/aiosqlite

@时间        :2020/07/28 22:36:05
@作者        :Riven
@版本        :1.0.0
'''

import os
import sqlite3

if __name__ == '__main__':
    path = os.getcwd() + '/app_server/data/data_base.db'

    # 1建立数据库
    # 1.1在硬盘上建立数据库
    db_connecter = sqlite3.connect(path)
    # 1.2在内存上建立数据库
    # db_connecter = sqlite3.connect('memory')

    # 2.创建游标
    db_cursor = db_connecter.cursor()

    # 3.执行sql语句
    # 3.1创建表 示例中所有的大写字符为SQL语法标准，小写字符为用户自定义的字符，但由于SQL语句不区分大小写，所以将SQL标准语句小写也可以。
    db_cursor.execute('CREATE TABLE IF NOT EXISTS account_list(id INTEGER PRIMARY KEY,phone TEXT,password TEXT,name TEXT,token TEXT)')

    # 3.2新增数据
    db_cursor.execute("INSERT INTO account_list (phone,password,name,token) \
      VALUES ('15012341234', '12345678', 'Paul', '123456789-098765432')")

    cur_cursor = db_cursor.execute("select * from account_list")
    for item in cur_cursor:
        print(item)

    db_connecter.commit()

    db_cursor.close()
    db_connecter.close()