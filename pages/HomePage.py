#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from util.BasePage import BasePage


class HomePage(BasePage):
    GEO_location_close = (By.XPATH, '//div[@id="wrapper"]/div[7]/div[2]/a')
    newsletter_popup_close = (By.CSS_SELECTOR, 'EDM-popUp > div.EDM-popUp-box > div > a.EDM-popUp-close.close_btn')
    login_text = (By.XPATH, "//li[@id='signin_li']/a/span")
    login_button = (By.XPATH, "//li[@id='signin_li']/div/div/span/a")
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    sign_in_butttn = (By.XPATH, "//form[@id='loginFormNew']/span")
    search_box = (By.ID, 'search_input')
    search_button = (By.ID, 'search_button')
