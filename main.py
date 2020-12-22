# -*- coding: utf-8 -*-
"""
 Created by Sakura.Gaara on  2020/12/17 18:49
"""
from mysql.mysql_backup import Backup
from mysql.mysql_load import Load
from settings import back_config, load_config

if __name__ == '__main__':
    backup = Backup(back_config)
    print(backup.dump_tables)
    print(backup.structure_table)
    backup.bakup_tables(backup.dump_tables)
    yorn = input("是否导入数据[y/n]:")
    if yorn.lower() == "y":
        load = Load(load_config)
        load.load_tables(backup.dump_tables)
    else:
        print('若需其他时间导入数据，可执行load.py完成导入.')
