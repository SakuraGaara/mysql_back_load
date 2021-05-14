# # -*- coding: utf-8 -*-
# """
#  Created by Sakura.Gaara on  2020/12/16 15:39
# """


# 默认备份结构和数据，structure_table只备份表结构
structure_table = [
    "table1",
    "table2"
]
# 忽略表
ignore_table = [
    "table3",
    "table4"
]
# 备份表存储目录
BACKUP_PATH="/data/backup/"
# 备份数据库连接配置
back_config = {
    'BACKUP_HOST': "127.0.0.1",
    'BACKUP_DB': "test",
    'BACKUP_USER': "root",
    'BACKUP_PASSWORD': "123456",
    'BACKUP_PORT': 3306
}
# 导入数据库连接配置
load_config = {
    'BACKUP_HOST': "127.0.0.1",
    'BACKUP_DB': "test1",
    'BACKUP_USER': "root",
    'BACKUP_PASSWORD': "123456",
    'BACKUP_PORT': 3306
}