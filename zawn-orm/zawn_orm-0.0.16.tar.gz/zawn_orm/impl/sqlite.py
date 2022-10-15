#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-08-25
# @Author  : wuxiangbin
# @Site    : www.0-9.ink
# @File    : sqlite.py
# @Software: orm
# @Function:
import sqlite3
from typing import List

from zawn_orm.database import Database, Query, Operation


class SQLite(Database):
    """ SQLite数据库的实现类 """

    database_type: str = 'sqlite'

    async def connect(self):
        self.connection = sqlite3.connect(':memory:')

    async def close(self):
        self.connection.commit()
        self.connection.close()
        self.connection = None

    async def on_search(self, query: Query):
        pass

    async def on_execute(self, operation_list: List[Operation]) -> dict:
        cursor = self.connection.cursor()
        cursor.executemany()
