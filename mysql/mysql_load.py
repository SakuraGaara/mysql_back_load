# -*- coding: utf-8 -*-
"""
 Created by Sakura.Gaara on  2020/12/18 14:23
"""
import os
import subprocess
import time
from mysql.libs import path_file, mysql_connect
from pylog import logger
from settings import BACKUP_PATH


class Load:
    def __init__(self, load_config):
        self.load_host = load_config['BACKUP_HOST']
        self.load_db = load_config['BACKUP_DB']
        self.load_user = load_config['BACKUP_USER']
        self.load_password = load_config['BACKUP_PASSWORD']
        self.load_port = load_config['BACKUP_PORT']
        self.load_path = BACKUP_PATH

        self.all_tables = mysql_connect(self.load_user, self.load_password, self.load_host, self.load_port,
                                        self.load_db)

    def exists_file(self, tb):
        load_file = path_file(self.load_path, tb)
        if os.path.exists(load_file):
            return load_file
        else:
            raise Exception('文件%s不存在.' % (load_file))

    def loadcmd(self, tb):
        load_file = self.exists_file(tb)
        load_cmd = 'mysql -u{} -p{} -h{} -P{} {} < {}'.format(self.load_user, self.load_password, self.load_host,
                                                              self.load_port, self.load_db, load_file)

        return load_cmd, load_file

    def cmd(self, command):
        start_time = time.time()
        subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
        while subp.poll() is None:
            time.sleep(1)
        if subp.poll() != 0:
            raise Exception("mysql 导入数据失败！！！", subp.communicate()[1])
        sleep_time = round(time.time() - start_time, 4)
        return subp, sleep_time

    def load_tables(self, tbs):
        result = {"success": [], "failed": []}
        starttime = time.time()
        logger.info("\n========================开始导入数据========================")
        for tb in tbs:
            load_cmd, load_file = self.loadcmd(tb)
            try:
                subp, sleep_time = self.cmd(load_cmd)
                result["success"].append(tb)
                logger.info("▄ %s -> %s -- 用时 %s seconds." % (load_file, tb, sleep_time))
            except Exception as e:
                logger.error(e)
                result["failed"].append(tb)
        logger.info(
            "\n========================导入数据结束========================\n总用时:%s seconds.\n成功:%d\n失败:%d\n结果:%s\n" % (
                round(time.time() - starttime, 4), len(result["success"]), len(result["failed"]), result))
        return result
