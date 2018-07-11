#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
得到当前页面所有连接
"""
import requests
import re
from selenium import webdriver

url = 'https://www.smartbuyglasses.co.uk'
r = requests.get(url)
r.encoding = 'utf-8'
# 利用 re
matchs = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", r.text)
for link in matchs:
    if link.find('www'):
        f = open('/Users/admin/test/test001.txt', 'r+')
        f.read()
        f.write(link + '\n')
    elif link.count('/', 0, 1) == 1:
        f = open('/Users/admin/test/test001.txt', 'r+')
        f.read()
        f.write('www.smartbuyglasses.co.uk'+link + '\n')
    elif link.find('https'):
        f = open('/Users/admin/test/test001.txt', 'r+')
        f.read()
        f.write(link + '\n')
    elif link.find('javascript'):
        pass
    else:
        pass


# 利用selenium（要开浏览器！）
# driver = webdriver.Firefox()
# driver.get(url)
# for link in driver.find_elements_by_tag_name("a"):
#     f = open('/Users/admin/test/test002.txt', 'r+')
#     f.seek(0, 2)
#     f.write(link.get_attribute("href"))
#     # print(link.get_attribute("href"))
# driver.close()
# f.close()


