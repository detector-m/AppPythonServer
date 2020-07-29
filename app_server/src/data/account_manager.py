#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :account_manager.py
@说明        :
@时间        :2020/07/24 23:03:27
@作者        :Riven
@版本        :1.0.0
'''
import os
import sqlite3

import sys
sys.path.append('.')
from app_server.src.data.data_interface import DataInterface
from app_server.src.data.data_adapter import DataAdapter

class AccountDataInterface(DataInterface):
    # def test(self):
    #     print(type(AccountDataInterface))
    #     print('DataM1, save')
    #     print(self.__class__.__name__ + ' ' + self.test.__class__.__name__)
    #     print(type(self.test))
    # def __init__(self, path):
    #     self.path = path
    pass

ACCOUNT_DB_TABLE_NAME = 'account_table'     
class AccountDataDB(AccountDataInterface):
    def save(self, save_data, path=None):
        print(self.__class__.__name__ + ' ' + self.save.__name__)

        if not path or not save_data:
            return None

        cur_con, cur_cur = self._connect(path)

        # cur_cur.execute(f"INSERT INTO {ACCOUNT_DB_TABLE_NAME} (phone,password,name,token) \
    #   VALUES ({save_data['phone']}, {save_data['password']}, {save_data['name']}, {save_data['token']})")
        cur_cur.execute("INSERT INTO account_table (phone,password,name,token) \
      VALUES ('15012341234', '12345678', 'Paul', '123456789-098765432')")
        cur_con.commit()

        cur_cur.close()
        cur_con.close()
                
    def fetch(self, fetch_data=None, path=None):
        print(self.__class__.__name__ + ' ' + self.fetch.__name__)

        if not path:
            return None

        cur_con, cur_cur = self._connect(path)

        if not fetch_data:
            cur_cur.execute("select * from account_table")
            for item in cur_cur:
                print(item)
        
        cur_cur.close()
        cur_con.close()

    '''
    建立/连接数据库
    '''
    def _connect(self, path):
        # 建立数据库
        cur_con = sqlite3.connect(path)
        # 获取游标
        cur_cur = cur_con.cursor()

        # 创建表
        cur_cur.execute('CREATE TABLE IF NOT EXISTS account_table (id INTEGER PRIMARY KEY,phone TEXT,password TEXT,name TEXT,token TEXT)')

        return (cur_con, cur_cur)


class AccountManager(DataAdapter):
    def __init__(self, data_interface: DataInterface, *, path=None):
        # super().__init__(data_interface)
        DataAdapter.__init__(self, data_interface)

        if not path:
            self.path = os.getcwd() + '/app_server/data/data_base.db'
        else:
            self.path = path
    

if __name__ == '__main__':
    save_data = {'phone': '15012340000', 'password': '000000', 'name': 'Riven', 'token': '123456',}
    print(f"INSERT INTO {ACCOUNT_DB_TABLE_NAME} (phone,password,name,token) \
      VALUES ({save_data['phone']}, {save_data['password']}, {save_data['name']}, {save_data['token']})")
    db = AccountDataDB()
    db_handler = AccountManager(db)
    db_handler.save({'phone': '15012340000', 'password': '000000', 'name': 'Riven', 'token': '123456',}, db_handler.path)
    db_handler.fetch(path=db_handler.path)
    # db_handler.save({}, 'a')