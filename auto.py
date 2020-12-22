# -*- coding: utf-8 -*-
"""
 Created by Sakura.Gaara on  2020/12/17 16:20
"""
from apscheduler.schedulers.blocking import BlockingScheduler

from mysql.mysql_backup import Backup
from mysql.mysql_load import Load
from settings import back_config, load_config


def job():
    backup = Backup(back_config)
    backup.bakup_tables(backup.dump_tables)

    load = Load(load_config)
    load.load_tables(backup.dump_tables)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', day_of_week='1-5', hour=1, minute=10)
    scheduler.start()
