# -*- coding: utf-8 -*-
"""
 Created by Sakura.Gaara on  2020/12/18 17:15
"""
from mysql.mysql_backup import Backup
from mysql.mysql_load import Load
from settings import load_config, back_config

if __name__ == '__main__':
    backup = Backup(back_config)
    load = Load(load_config)
    load.load_tables(backup.dump_tables)
