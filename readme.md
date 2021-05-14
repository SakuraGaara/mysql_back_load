## mysql_back_load 备份导出，导入

脚本的初衷是预发环境要与线上环境部分一直，所以经常要将线上环境的部分数据同步到预发环境

备份导出和导入主要通过mysql/mysql_backup.py 和mysql/mysql_load完成.py，备份单张表一个文件

### settings.py
- structure_table: 默认备份表和数据，structure_table中添加表名，则只备份表结构
- ignore_table: ignore_table中添加表名，则不进行任何备份
- back_config: 备份数据库的连接信息
- load_config: 导入数据库的连接信息
- BACKUP_PATH: 备份文件路径,默认/data/backup
- auto.py: 可自行修改定期备份时间


### 启动方式
定时备份->导入
```python auto.py```

手动备份->导入
```python main.py```

### Docker方式
修改设置structure_table/ignore_table/back_config/load_config/BACKUP_PATH/auto.py等信息

```
docker build -t mysql_back_load:v1 .
docker run -d -name mysql_back_load -v /data/backup:/data/backup mysql_back_load:v1
```
