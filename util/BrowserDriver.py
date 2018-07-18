#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os.path
from selenium import webdriver
from util.logger import Logger
import yaml

logger = Logger(logger="BrowserDriver").getlog()


class BrowserDriver(object):
    # 这是获取相对路径的方法
    path = os.path.dirname(os.path.abspath(''))
    chrome_driver_path = '/usr/local/bin/chromedriver'
    ie_driver_path = path + '/driver/IEDriverServer.exe'
    edge_driver_path = path + '/driver/MicrosoftWebDriver.exe'
    opera_driver_path = path + '/driver/operadriver.exe'
    safari_driver_path = path + '/driver/safaridriver.exe'

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        # 读取配置文件
        file_path = os.path.dirname(os.getcwd())
        name_path = file_path + '/yaml/browser.yaml'
        with open(name_path, 'r') as f:
            temp = yaml.load(f.read())
        # 获取配置文件属性
        brow = temp['browserType']['browserName']
        browser = brow
        logger.info("选择的浏览器为: %s 浏览器" % browser)
        url = temp['WebUrl']['URL']
        logger.info("打开的URL为: %s" % url)
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("启动火狐浏览器")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("启动谷歌浏览器")
        elif browser == "IE":
            driver = webdriver.IE(self.ie_driver_path)
            logger.info("启动IE浏览器")
        elif browser == "Edge":
            driver = webdriver.Edge(self.edge_driver_path)
            logger.info("启动Edge浏览器")
        elif browser == "Opera":
            driver = webdriver.Opera(self.opera_driver_path)
            logger.info("启动Opera浏览器")
        elif browser == "Safari":
            driver = webdriver.Safari(self.safari_driver_path)
            logger.info("启动Safari浏览器")
        driver.maximize_window()
        driver.set_window_size(1440, 900)
        logger.info("全屏当前窗口")
        driver.implicitly_wait(5)
        logger.info("设置5秒隐式等待时间")
        driver.get(url)
        logger.info("打开URL: %s" % url)
        return driver

    def quit_browser(self):
        logger.info("关闭浏览器")
        self.driver.quit()
