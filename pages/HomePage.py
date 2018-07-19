#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from util.BasePage import BasePage


class HomePage(BasePage):
    geo_location_close = (By.XPATH, '//div[@id="wrapper"]/div[7]/div[2]/a')
    newsletter_popup_close = (By.CSS_SELECTOR, 'EDM-popUp > div.EDM-popUp-box > div > a.EDM-popUp-close.close_btn')
    login_text = (By.XPATH, "//li[@id='signin_li']/a/span")
    login_button = (By.XPATH, "//li[@id='signin_li']/div/div/span/a")
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    sign_in_button = (By.XPATH, "//form[@id='loginFormNew']/span")
    search_box = (By.ID, 'search_input')
    search_button = (By.ID, 'search_button')
    menu_sunglasses = (By.CSS_SELECTOR, '#menuN_1 > a')
    menu_glasses = (By.CSS_SELECTOR, "#menuN_2 > a")
    menu_cl = (By.CSS_SELECTOR, "#menuN_5 > a")
    menu_explore = (By.CSS_SELECTOR, "#menuN_6 > a")
    menu_deals = (By.CSS_SELECTOR, "#menuN_7 > a")
    menu_sunglasses_men = (By.CSS_SELECTOR, "#menuN_level_1 > li > div > div.shop_by_left > ul:nth-child(2) > li:nth-child(1) > a")
    menu_sunglasses_women = (By.CSS_SELECTOR, "# menuN_level_1 > li > div > div.shop_by_left > ul:nth-child(2) > li:nth-child(2) > a")
    top_sellers_sun_1 = (By.XPATH, "//ul[@id='pro_slider_sunglasses']/li/a")
    top_sellers_eye_1 = (By.XPATH, "//ul[@id='pro_slider_eyeglasses']/li/a")

