#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pymysql
from util.BaseUtil import BaseUtil

db_host = BaseUtil.get_config_value("MySql", "host")
port = BaseUtil.get_config_value("MySql", "port")
username = BaseUtil.get_config_value("MySql", "username")
password = BaseUtil.get_config_value("MySql", "password")
db_name = BaseUtil.get_config_value("MySql", "db_name")
charset = BaseUtil.get_config_value("MySql", "charset")


class MysqlDB:

    @staticmethod
    def connect_db():
        # 打开连接数据库
        db = pymysql.connect(host=db_host,
                             port=port,
                             user=username,
                             password=password,
                             database=db_name,
                             use_unicode=True,
                             charset=charset)
        return db
