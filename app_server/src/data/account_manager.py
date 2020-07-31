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

        self.cur = None
        self.con = None

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
            print(sql_str)

            self.cur.execute(sql_str)
            self.con.commit()

            return 1
        except Exception as e:
            print(e)
            self.close()
            return 0

    '''
    更新数据
    '''
    def update(self, **kwargs) -> int:
        if not self.con:
            return -1;

        if not kwargs:
            return -1;

        try:
            # sql_str = f"UPDATE {ACCOUNT_DB_TABLE_NAME} SET "
            # key_str =''
            # for key, value in kwargs.items():
            #     if key == ACCOUNT_DB_TABLE_KEYS[0]:
            #         continue
                
            #     # if not value:
            #     #     value = "''"
            #         # continue
            #     # key_str += f"'{str(key)}'" + "=" + f"'{str(value)}'" + ", "
            #     key_str += str(key) + "=" + f"'{str(value)}'" + ", "


            # if not key_str:
            #     return 0
            
            # key_str = key_str[:-2]
            # key_str += f" WHERE {ACCOUNT_DB_TABLE_KEYS[0]}='{kwargs[ACCOUNT_DB_TABLE_KEYS[0]]}'"

            # sql_str = sql_str + key_str
            # print(sql_str)

            # self.cur.execute(sql_str)

            # ？占位符方式
            sql_str = f"UPDATE {ACCOUNT_DB_TABLE_NAME} SET "
            keys = list(kwargs.keys())
            values = list(kwargs.values())

            # keys.remove(ACCOUNT_DB_TABLE_KEYS[0])
            # values.remove(kwargs[ACCOUNT_DB_TABLE_KEYS[0]])

            keys_str = "=?, ".join(keys)
            keys_str += "=? "
            keys_str += f"WHERE {ACCOUNT_DB_TABLE_KEYS[0]}=?"
            values.append(kwargs[ACCOUNT_DB_TABLE_KEYS[0]])
            sql_str += keys_str
            print(sql_str)

            self.cur.execute(sql_str, tuple(values))
            self.con.commit()

            return 1
        except Exception as e:
            print(e)
            self.close()
            return 0

    '''
    删除
    '''
    def delete(self, **kwargs):
        if not self.con:
            return -1;
        
        if not kwargs:
            return -1

        keys = list(kwargs.keys())
        # print(keys)
        key = keys[0]
        if key not in ACCOUNT_DB_TABLE_KEYS:
            return -1
        
        account_list = []
        # sql_str = f"DELETE * FROM {ACCOUNT_DB_TABLE_NAME} WHERE {key}='{kwargs[key]}'"
        # self.cur.execute(sql_str)

        sql_str = f"DELETE FROM {ACCOUNT_DB_TABLE_NAME} WHERE {key}=?"
        print(sql_str)
        self.cur.execute(sql_str, (kwargs[key], ))
        self.con.commit()

        return 1


    '''
    根据电话号码判读是否存在
    '''   
    def exist(self, phone):
        if not self.con:
            return False;

        if not phone:
            return False
        
        exist_list = self.fetch(**{ACCOUNT_DB_TABLE_KEYS[0]: phone})
        if not exist_list:
            return False

        return True



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
                item_dict = {}
                item_dict['id'] = item[0]
                for i, vale in enumerate(item[1:]):
                    item_dict[ACCOUNT_DB_TABLE_KEYS[i]] = vale
                
                account_list.append(item_dict)

            return account_list

    def fetch_all(self):
        return self.fetch()


class AccountManager(DataAdapter):
    def __init__(self, data_interface: DataInterface=None, *, path=None):
        # if not data_interface:
            # data_interface = AccountDataDB()

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
    # print(fetch_dic)
    exist_list = account_db_manager.fetch(**fetch_dic)
    if not exist_list:
        account_db_manager.insert(**save_data)

    save_data = {'phone': '15012340001', 'password': '000001', 'name': 'Jobs', 'token': ''} 
    fetch_dic = {'phone': save_data['phone']}
    # print(fetch_dic)
    exist_list = account_db_manager.fetch(**fetch_dic)   
    if not exist_list:
        account_db_manager.insert(**save_data)

    # account_list = account_db_manager.fetch(**{'phone': '15012340000'})
    # print(account_list)

    account_list = account_db_manager.fetch_all()
    print(account_list)

    save_data = {'phone': '15012340003', 'password': '444444', 'name': 'Jobs444444', 'token': ''} 
    fetch_dic = {'phone': save_data['phone']}
    # print(fetch_dic)
    exist_list = account_db_manager.fetch(**fetch_dic)   
    if exist_list:
        account_db_manager.update(**save_data)
    
    account_list = account_db_manager.fetch_all()
    print(account_list)

    if account_db_manager.exist('15012340001'):
        account_db_manager.delete(**{'phone': '15012340001'})

    account_list = account_db_manager.fetch_all()
    print(account_list)
