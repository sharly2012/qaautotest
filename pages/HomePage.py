#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from util.BasePage import BasePage


class HomePage(BasePage):
    geo_cnt = (By.CLASS_NAME, 'geo-cnt')
    geo_close_btn = (By.CLASS_NAME, 'geo-close-btn')
    EDM_popUp_cnt = (By.CLASS_NAME, "EDM-popUp-cnt")
    EDM_popUp_close_btn = (By.CLASS_NAME, "EDM-popUp-close close_btn")
    login_text = (By.XPATH, "//li[@id='signin_li']/a/span")
    login_button = (By.XPATH, "//li[@id='signin_li']/div/div/span/a")
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    sign_in_button = (By.XPATH, "//form[@id='loginFormNew']/span")
    search_box = (By.ID, 'search_input')
    search_button = (By.ID, 'search_button')
    menu_sunglasses = (By.CSS_SELECTOR, '#menuN_1 > a')
    sun_man = (By.XPATH, "//ul[@id='menuN_level_1']/li/div/div[1]/ul[1]/li[1]/a")
    menu_glasses = (By.CSS_SELECTOR, "#menuN_2 > a")
    menu_cl = (By.CSS_SELECTOR, "#menuN_5 > a")
    menu_explore = (By.CSS_SELECTOR, "#menuN_6 > a")
    menu_deals = (By.CSS_SELECTOR, "#menuN_7 > a")
    menu_sunglasses_men = (
    By.CSS_SELECTOR, "#menuN_level_1 > li > div > div.shop_by_left > ul:nth-child(2) > li:nth-child(1) > a")
    menu_sunglasses_women = (
    By.CSS_SELECTOR, "# menuN_level_1 > li > div > div.shop_by_left > ul:nth-child(2) > li:nth-child(2) > a")
    top_sellers_sun_1 = (By.XPATH, "//ul[@id='pro_slider_sunglasses']/li/a")
    top_sellers_eye_1 = (By.XPATH, "//ul[@id='pro_slider_eyeglasses']/li/a")
    your_account = (By.XPATH, "//li[@id='signin_li_already']/a")
    user_detail = (By.XPATH, "//li[@id='signin_li_already']/div/div/p[1]")
    search_pop_1 = (By.XPATH, "//from[@id='search']/div/div[1]/div/div[1]/div/div[2]/a/div[1]")
    search_result = (By.XPATH, "//div[@id='content']/div[2]/div[3]/div[2]/div[1]/div[1]/ul/li[3]/a[2]/div[1]/p")

    def close_geo_popup(self):
        try:
            if self.is_visibility(self.geo_cnt):
                self.click(self.geo_close_btn)
        except NoSuchElementException as e:
            self.logger.error("Not found GEO pop-up. ---%s" % e)

    def close_newsletter_popup(self):
        try:
            if self.is_visibility(self.EDM_popUp_cnt):
                self.click(self.EDM_popUp_close_btn)
        except NoSuchElementException as e:
            self.logger.error("Not found newsletter pop-up. ---%s" % e)
