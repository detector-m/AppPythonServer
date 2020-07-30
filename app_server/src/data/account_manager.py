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
from app_server.src.data.data_constant import DATA_DB_PATH, ACCOUNT_DB_TABLE_NAME, ACCOUNT_DB_TABLE_KEYS
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
    def save(self, save_data, path=None):
        # raise NotImplementedError
        pass

    def fetch(self, fetch_data=None, path=None):
        # raise NotImplementedError
        pass

class AccountDataDB(AccountDataInterface):
    def __init__(self, path=None):
        AccountDataInterface.__init__(self)
        self.path = path
    
    '''
    创建/连接数据库
    '''
    def connect(self):
        if not self.path:
            return None
        
        # 建立数据库
        self.con = sqlite3.connect(self.path)
        # 获取游标
        self.cur = self.con.cursor()

        # 创建表
        sql_str = f"CREATE TABLE IF NOT EXISTS {ACCOUNT_DB_TABLE_NAME} (id INTEGER PRIMARY KEY, {ACCOUNT_DB_TABLE_KEYS[0]} TEXT, {ACCOUNT_DB_TABLE_KEYS[1]} TEXT, {ACCOUNT_DB_TABLE_KEYS[2]} TEXT, {ACCOUNT_DB_TABLE_KEYS[3]} TEXT)"
        self.cur.execute(sql_str)
        self.con.commit()

        return (self.con, self.cur)

    '''
    关闭数据库
    '''
    def close(self):
        if not self.con:
            return
        
        self.cur.close()
        self.con.close()

    '''
    插入数据
    '''
    def insert(self, **kwargs) -> int:
        if not self.con:
            return -1;

        if not kwargs:
            return -1;

        # fetch_dic = dict([(ACCOUNT_DB_TABLE_KEYS[0], kwargs[ACCOUNT_DB_TABLE_KEYS[0]])]);
        # fetch_dic = {ACCOUNT_DB_TABLE_KEYS[0]: kwargs[ACCOUNT_DB_TABLE_KEYS[0]]}
        # print(fetch_dic)
        # exits_list = self.fetch(**fetch_dic)
        # if exits_list:
        #     return 0

        try:
            sql_str = f"INSERT INTO {ACCOUNT_DB_TABLE_NAME} ({ACCOUNT_DB_TABLE_KEYS[0]}, {ACCOUNT_DB_TABLE_KEYS[1]}, {ACCOUNT_DB_TABLE_KEYS[2]}, {ACCOUNT_DB_TABLE_KEYS[3]}) \
            VALUES ('{kwargs[ACCOUNT_DB_TABLE_KEYS[0]]}', '{kwargs[ACCOUNT_DB_TABLE_KEYS[1]]}', '{kwargs[ACCOUNT_DB_TABLE_KEYS[2]]}', '{kwargs[ACCOUNT_DB_TABLE_KEYS[3]]}')"
            self.cur.execute(sql_str)
            self.con.commit()
            return 1
        except Exception as e:
            print(e)
            self.close()
            return 0

    
    '''
    获取数据
    '''
    def fetch(self, **kwargs):
        if not self.con:
            return None;

        if not kwargs:
            account_list = []
            sql_str = f"SELECT * FROM {ACCOUNT_DB_TABLE_NAME}"
            self.cur.execute(sql_str)
            for item in self.cur:
                account_list.append(item)

            return account_list
        else:
            keys = list(kwargs.keys())
            # print(keys)
            key = keys[0]
            if key not in ACCOUNT_DB_TABLE_KEYS:
                return None
            
            account_list = []
            sql_str = f"SELECT * FROM {ACCOUNT_DB_TABLE_NAME} WHERE {key}='{kwargs[key]}'"
            self.cur.execute(sql_str)
            for item in self.cur:
                account_list.append(item)

            return account_list
    

    # def save(self, save_data, path=None):
    #     print(self.__class__.__name__ + ' ' + self.save.__name__)

    #     if not path or not save_data:
    #         return None

    #     cur_con, cur_cur = self._connect(path)

    #     # cur_cur.execute(f"INSERT INTO {ACCOUNT_DB_TABLE_NAME} (phone,password,name,token) \
    # #   VALUES ({save_data['phone']}, {save_data['password']}, {save_data['name']}, {save_data['token']})")
    #     cur_cur.execute(f"INSERT INTO {ACCOUNT_DB_TABLE_NAME} (phone,password,name,token) \
    #   VALUES ('{save_data['phone']}', '{save_data['password']}', '{save_data['name']}', '{save_data['token']}')")

    #     # cur_cur.execute("INSERT INTO account_table (phone,password,name,token) \
    # #   VALUES ('15012341234', '12345678', 'Paul', '123456789-098765432')")
    #     cur_con.commit()

    #     cur_cur.close()
    #     cur_con.close()
                
    # def fetch(self, fetch_data=None, path=None):
    #     print(self.__class__.__name__ + ' ' + self.fetch.__name__)

    #     if not path:
    #         return None

    #     cur_con, cur_cur = self._connect(path)

    #     if not fetch_data:
    #         cur_cur.execute("select * from account_table")
    #         for item in cur_cur:
    #             print(item)
        
    #     cur_cur.close()
    #     cur_con.close()


class AccountManager(DataAdapter):
    def __init__(self, data_interface: DataInterface, *, path=None):
        # super().__init__(data_interface)
        DataAdapter.__init__(self, data_interface)

        if not path:
            self.data_interface.path = os.getcwd() + DATA_DB_PATH
        else:
            self.data_interface.path = path
    

if __name__ == '__main__':
    account_db_handler = AccountDataDB()
    account_db_manager = AccountManager(account_db_handler)
    account_db_manager.connect()

    save_data = {'phone': '15012340000', 'password': '000000', 'name': 'Riven', 'token': ''}
    # fetch_dic = dict([(ACCOUNT_DB_TABLE_KEYS[0], kwargs[ACCOUNT_DB_TABLE_KEYS[0]])]);
    fetch_dic = {'phone': save_data['phone']}
    print(fetch_dic)
    exits_list = account_db_manager.fetch(**fetch_dic)
    if not exits_list:
        account_db_manager.insert(**save_data)

    save_data = {'phone': '15012340001', 'password': '000001', 'name': 'Jobs', 'token': ''} 
    fetch_dic = {'phone': save_data['phone']}
    print(fetch_dic)
    exits_list = account_db_manager.fetch(**fetch_dic)   
    if not exits_list:
        account_db_manager.insert(**save_data)

    account_list = account_db_manager.fetch(**{'phone': '15012340000'})
    print(account_list)

    # print(account_db_handler.path)

    # db_handler.save({'phone': '15012340000', 'password': '000000', 'name': 'Riven', 'token': '123456',}, db_handler.path)
    # db_handler.fetch(path=db_handler.path)
    # db_handler.save({}, 'a')