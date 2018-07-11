#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os.path
from selenium import webdriver
import yaml
from util.logger import Logger

logger = Logger(logger="Chrome_mobile").getlog()


class MobileDriver(object):
    # chrome_driver_path = path + '/driver/chromedriver.exe'
    chrome_driver_path = '/usr/local/bin/chromedriver'

    def __init__(self, driver):
        self.driver = driver

    def open_mobile_browser(self):
        file_path = os.path.dirname(os.getcwd())
        name_path = file_path + '/yaml/browser.yaml'
        with open(name_path, 'r') as f:
            temp = yaml.load(f.read())
        # 获取配置文件属性
        brow = temp['browserType']['browserName']
        browser = brow
        logger.info("选择的浏览器为: %s 浏览器" % browser)
        url = temp['WebUrl']['URL']
        mobile_emulation = {'deviceName': 'iPhone X'}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('mobileEmulation', mobile_emulation)
        driver = webdriver.Chrome(self.chrome_driver_path, options=chrome_options)
        driver.implicitly_wait(30)
        driver.maximize_window()
        logger.info("Open mobile model successfully")
        driver.get(url)
        return driver

    def quit_browser(self):
        self.driver.quit()
        logger.info("退出浏览器")
