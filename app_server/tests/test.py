#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :test.py
@说明        :
@时间        :2020/07/22 17:09:59
@作者        :Riven
@版本        :1.0.0
'''

from typing import (
    Any,
    AsyncIterator,
    Callable,
    Generator,
    Iterable,
    Optional,
    Type,
    Union,
)

import asyncio
import threading

class B:
    def __iter__(self):
        return self
    def __next__(self):
        raise StopIteration('end')


class A:
    def __await__(self):
        print('__await__-------start')
        t = self.test()
        print(t)
        print('__await__-------end')
        return t.__await__()
        # asyncio.sleep(1)
        # return self.__await__()

    async def test(self):
        await asyncio.sleep(1)
        return self

    async def good(self):
        await asyncio.sleep(2)
        print('22222')
        return 500

async def a():
    s = await A()
    # s = A()
    print(s)

    s1 = await s
    print(s1)

    # t1 = await s.good()
    # print(t1)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(a())
    loop.close()