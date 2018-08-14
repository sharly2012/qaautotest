#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os.path
from selenium import webdriver
import yaml
from util.logger import Logger
from util.BaseUtil import BaseUtil

logger = Logger(logger="Chrome_mobile").get_log()


class MobileDriver(object):
    file_path = BaseUtil.get_root_path()
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
        chrome_driver_path = file_path + '/driver/linux/chromedriver'
    elif system_name == 'MacOS':
        chrome_driver_path = file_path + '/driver/MacOS/chromedriver'
    elif system_name == 'Windows':
        chrome_driver_path = file_path + '/driver/Windows/chromedriver.exe'

    def __init__(self, driver):
        self.driver = driver

    def open_mobile_browser(self):

        mobile_emulation = {'deviceName': 'iPhone X'}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('mobileEmulation', mobile_emulation)
        driver = webdriver.Chrome(self.chrome_driver_path, options=chrome_options)
        driver.implicitly_wait(30)
        driver.set_window_size(1440, 900)
        logger.info("Open mobile model successfully")
        driver.get(self.url)
        return driver

    def quit_browser(self):
        self.driver.quit()
        logger.info("退出浏览器")
