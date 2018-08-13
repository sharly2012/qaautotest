#!/usr/bin/python3
# -*- coding: utf-8 -*-
import yaml
from selenium import webdriver
from util.logger import Logger
from util.config import GlobalVar


logger = Logger(logger="BrowserDriver").get_log()


class BrowserDriver(object):
    # file_path = os.path.dirname(os.path.abspath('.'))
    file_path = GlobalVar.get_root_path()
    name_path = file_path + '/yaml/browser.yaml'
    with open(name_path, 'r') as f:
        temp = yaml.load(f.read())
    system_name = temp['OperatingSystem']['systemName']
    logger.info("当前系统为" + system_name)
    browser = temp['browserType']['browserName']
    logger.info("选择的浏览器为: %s 浏览器" % browser)
    url = temp['WebUrl']['URL']
    logger.info("打开的URL为: %s" % url)
    if system_name == 'Linux':
        firefox_driver_path = file_path + '/driver/linux/geckodriver'
        chrome_driver_path = file_path + '/driver/linux/chromedriver'
        opera_driver_path = file_path + '/driver/linux/operadriver.exe'
    elif system_name == 'MacOS':
        firefox_driver_path = file_path + '/driver/MacOS/geckodriver'
        chrome_driver_path = file_path + '/driver/MacOS/chromedriver'
        opera_driver_path = file_path + '/driver/MacOS/operadriver'
    elif system_name == 'Windows':
        firefox_driver_path = file_path + '/driver/Windows/geckodriver.exe'
        chrome_driver_path = file_path + '/driver/Windows/chromedriver.exe'
        ie_driver_path = file_path + '/driver/Windows/IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        if self.browser == "Firefox":
            driver = webdriver.Firefox(log_path=self.file_path + "/logs/" + "geckodriver.log")
            logger.info("启动火狐浏览器")
        elif self.browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("启动谷歌浏览器")
        elif self.browser == "IE":
            driver = webdriver.IE(self.ie_driver_path)
            logger.info("启动IE浏览器")
        elif self.browser == "Edge":
            driver = webdriver.Edge(self.edge_driver_path)
            logger.info("启动Edge浏览器")
        elif self.browser == "Opera":
            driver = webdriver.Opera(self.opera_driver_path)
            logger.info("启动Opera浏览器")
        elif self.browser == "Safari":
            driver = webdriver.Safari(self.safari_driver_path)
            logger.info("启动Safari浏览器")
        # driver.maximize_window()
        driver.set_window_size(1440, 900)
        logger.info("全屏当前窗口")
        driver.implicitly_wait(5)
        logger.info("设置5秒隐式等待时间")
        driver.get(self.url)
        logger.info("打开URL: %s" % self.url)
        return driver

    def quit_browser(self):
        logger.info("关闭浏览器")
        self.driver.quit()
