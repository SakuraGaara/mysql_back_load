# -*- coding: utf-8 -*-
"""
 Created by Sakura.Gaara on  2020/12/16 15:35
"""
import os
import subprocess
import time

from mysql.libs import path_file, dump_tables, structure_tables
from pylog import logger

from settings import BACKUP_PATH


class Backup:
    def __init__(self, back_config):
        self.backup_host = back_config['BACKUP_HOST']
        self.backup_db = back_config['BACKUP_DB']
        self.backup_user = back_config['BACKUP_USER']
        self.backup_password = back_config['BACKUP_PASSWORD']
        self.backup_port = back_config['BACKUP_PORT']
        self.backup_path = BACKUP_PATH

        self.dump_tables = dump_tables(self.backup_user, self.backup_password, self.backup_host, self.backup_port,
                                       self.backup_db)
        self.structure_table = structure_tables()
        if not os.path.exists(self.backup_path):
            os.mkdir(self.backup_path)

    def exists_table(self, tb):
        """判断是否导入表数据"""
        return True if tb in self.dump_tables and tb in self.structure_table else False

    def dumpcmd(self, tb):
        backup_file = path_file(self.backup_path, tb)
        if self.exists_table(tb):
            dump_cmd = 'mysqldump -u{} -p{} -h{} -P{} --set-gtid-purged=off -d {} --tables {} > {}'.format(
                self.backup_user,
                self.backup_password,
                self.backup_host,
                self.backup_port,
                self.backup_db, tb,
                backup_file)
        else:
            dump_cmd = 'mysqldump -u{} -p{} -h{} -P{} --set-gtid-purged=off {} --tables {} > {}'.format(
                self.backup_user,
                self.backup_password,
                self.backup_host,
                self.backup_port,
                self.backup_db,
                tb,
                backup_file)
        return dump_cmd, backup_file

    def cmd(self, command):
        start_time = time.time()
        subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
        while subp.poll() is None:
            time.sleep(1)
        if subp.poll() != 0:
            raise Exception("mysqldump导出数据表失败", subp.communicate()[1])
        sleep_time = round(time.time() - start_time, 4)
        return subp, sleep_time

    def bakup_tables(self, tbs):
        result = {"success": [], "failed": []}
        starttime = time.time()
        logger.info("\n========================开始导出数据========================")
        for tb in tbs:
            dump_cmd, backup_file = self.dumpcmd(tb)
            try:
                subp, sleep_time = self.cmd(dump_cmd)
                result["success"].append(tb)
                logger.info("▄ %s -> %s -- 用时 %s seconds." % (tb, backup_file, sleep_time))
            except Exception as e:
                logger.error(e)
                result["failed"].append(tb)
        logger.info(
            "\n========================导出数据结束========================\n总用时:%s seconds.\n成功:%d\n失败:%d\n结果:%s\n" % (
                round(time.time() - starttime, 4), len(result["success"]), len(result["failed"]), result))
        return result
