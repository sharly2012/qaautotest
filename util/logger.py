#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import time
from util.config import GlobalVar


class Logger(object):
    def __init__(self, logger):
        """
        将日志保存到指定的路径文件中
        指定日志的级别，以及调用文件
        """

        # 创建logger文件
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handle，用来写入日志文件
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        # log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        log_path = GlobalVar.get_root_path() + '/logs/'
        log_name = log_path + now + '.log'

        file_handle = logging.FileHandler(log_name, encoding="utf-8")
        file_handle.setLevel(logging.INFO)

        # 创建一个handle，用来输入日志到控制台
        control_handle = logging.StreamHandler()
        control_handle.setLevel(logging.INFO)

        # 将输出的hangdle格式进行转换
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        file_handle.setFormatter(formatter)
        control_handle.setFormatter(formatter)

        # 给logger添加handle
        self.logger.addHandler(file_handle)
        self.logger.addHandler(control_handle)

    def get_log(self):
        return self.logger
