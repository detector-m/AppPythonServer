#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :plist_utils.py
@说明        :
@时间        :2020/07/27 19:25:50
@作者        :Riven
@版本        :1.0.0
'''
import plistlib

def read_content(path) -> dict:
    if not path:
        return None

    with open(path, 'rb') as fp:
        try:
            ret_dict = plistlib.load(fp)
        # except:
            # print(sys.exc_info())
        except plistlib.InvalidFileException as e:
            return None
    
    return ret_dict

def write_content(path, content: dict):
    if not path or not content:
        return

    with open(path, 'wb') as fp:
        plistlib.dump(content, fp)
