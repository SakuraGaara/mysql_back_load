# -*- coding: utf-8 -*-
"""
 Created by Sakura.Gaara on  2020/12/18 14:42
"""
import os

import pymysql

from pylog import logger
from settings import ignore_table, structure_table


def path_file(path, tb):
    return os.path.join(path, tb + '.sql')


# 获取所有表
def mysql_connect(user, password, host, port, db):
    all_tables = []
    try:
        conn = pymysql.connect(user=user, passwd=password, host=host,
                               port=port, database=db)
        cursor = conn.cursor()
        cursor.execute("show tables")
        data = cursor.fetchall()
        for table in data:
            all_tables.append(table[0])
        cursor.close()
        conn.close()
        return all_tables
    except Exception as e:
        logger.error("数据库连接失败, 请检查: %s" % e)


# 排除忽略表
def dump_tables(user, password, host, port, db):
    result = mysql_connect(user, password, host, port, db)
    for tb in ignore_table:
        result.remove(tb) if tb in result else ""
    return result


# 若忽略表与只同步结构表重复，则忽略
def structure_tables():
    for tb in ignore_table:
        structure_table.remove(tb) if tb in structure_table else ""
    return structure_table
