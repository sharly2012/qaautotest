#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from selenium.webdriver.common.action_chains import ActionChains


class HomepageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "https://www.smartbuyglasses.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_homepage(self):
        driver = self.driver
        driver.get("https://www.smartbuyglasses.com/")
        self.move_to(driver.find_element_by_link_text("SUNGLASSES"))
        driver.find_element_by_link_text("Men").click()
        self.assertTitle("Men's Sunglasses | Buy Online at SmartBuyGlasses USA")

        self.move_to(driver.find_element_by_link_text("SUNGLASSES"))
        driver.find_element_by_link_text("Women").click()
        self.assertTitle("Women's Sunglasses | Buy Online at SmartBuyGlasses USA")

        self.move_to(driver.find_element_by_link_text("SUNGLASSES"))
        driver.find_element_by_link_text("Aviator").click()
        self.assertTitle("Aviator Sunglasses | Buy Online at SmartBuyGlasses USA")

        self.move_to(driver.find_element_by_link_text("SUNGLASSES"))
        driver.find_element_by_link_text("Rectangle").click()
        self.assertTitle("Rectangle Sunglasses | Buy Online at SmartBuyGlasses USA")

        self.move_to(driver.find_element_by_link_text("SUNGLASSES"))
        driver.find_element_by_link_text("Oversized").click()
        self.assertTitle("Oversized Sunglasses | Buy Online at SmartBuyGlasses USA")

        self.move_to(driver.find_element_by_link_text("SUNGLASSES"))
        driver.find_element_by_link_text("Plastic").click()
        self.assertTitle("Plastic Sunglasses | Buy Online at SmartBuyGlasses USA")

        self.move_to(driver.find_element_by_link_text("SUNGLASSES"))
        driver.find_element_by_link_text("Titanium").click()
        self.assertTitle("Titanium Sunglasses | Buy Online at SmartBuyGlasses USA")

        self.move_to(driver.find_element_by_link_text("SUNGLASSES"))
        driver.find_element_by_link_text("Premium Acetate").click()
        self.assertTitle("Premium Acetate Sunglasses | Buy Online at SmartBuyGlasses USA")

        self.move_to(driver.find_element_by_link_text("SUNGLASSES"))
        driver.find_element_by_link_text("$ 0 ~ $ 50").click()
        self.assertTitle("Sunglasses | Buy Online at SmartBuyGlasses USA")

        self.move_to(driver.find_element_by_link_text("SUNGLASSES"))
        driver.find_element_by_link_text("Fast Shipping").click()
        self.assertTitle("Designer Sunglasses - Fast Shipping | SmartBuyGlasses USA")

        self.move_to(driver.find_element_by_link_text("SUNGLASSES"))
        driver.find_element_by_link_text("New Arrival").click()
        self.assertTitle("New Arrival Sunglasses | Buy Online at SmartBuyGlasses USA")

        self.move_to(driver.find_element_by_link_text("SUNGLASSES"))
        driver.find_element_by_link_text("Prescription").click()
        self.assertTitle("Prescription Sunglasses | Buy Online at SmartBuyGlasses USA")

        self.move_to(driver.find_element_by_link_text("SUNGLASSES"))
        driver.find_element_by_link_text("Sports").click()
        self.assertTitle("Sports Sunglasses | Buy Online at SmartBuyGlasses USA")

        self.move_to(driver.find_element_by_link_text("SUNGLASSES"))
        driver.find_element_by_link_text("Ski Goggles").click()
        self.assertTitle("Ski Goggles Sunglasses | Buy Online at SmartBuyGlasses USA")

        # driver.find_element_by_xpath("//div[@id='top_sun_glass_list']/ul/li/a/img").click()
        # driver.find_element_by_xpath("//div[@id='top_sun_glass_list']/ul/li[3]/a/img").click()
        # driver.find_element_by_xpath("//div[@id='top_sun_glass_list']/ul/li[6]/a/img").click()
        # driver.find_element_by_xpath("//div[@id='top_sun_glass_list']/ul/li[14]/a/img").click()
        # driver.find_element_by_link_text("Linda Farrow").click()
        # driver.find_element_by_link_text("SmartBuyGlasses").click()
        # driver.find_element_by_id("logo").click()
        # driver.find_element_by_xpath(
        #     u"(//area[@onclick=\"dataLayer.push({'event':'GAEvent', 'eventCategory': 'Home Banner', 'eventAction': 'click', 'eventLabel': ‘Default banner 2 - Desktop'})\"])[2]").click()
        # driver.find_element_by_xpath(
        #     u"(//area[@onclick=\"dataLayer.push({'event':'GAEvent', 'eventCategory': 'Home Banner', 'eventAction': 'click', 'eventLabel': ‘Default banner 2 - Desktop'})\"])[2]").click()
        # driver.find_element_by_xpath("//img[@alt='EYE-HP-Banner-D-EN']").click()
        # driver.find_element_by_xpath("//div[@id='pagenavi']/ul/li[2]").click()
        # driver.find_element_by_xpath(
        #     u"(//area[@onclick=\"dataLayer.push({'event':'GAEvent', 'eventCategory': 'Home Banner', 'eventAction': 'click', 'eventLabel': ‘Default banner 2 - Desktop'})\"])[2]").click()
        # driver.find_element_by_xpath("//div[@id='pagenavi']/ul/li[3]").click()
        # driver.find_element_by_xpath(
        #     u"(//area[@onclick=\"dataLayer.push({'event':'GAEvent', 'eventCategory': 'Home Banner', 'eventAction': 'click', 'eventLabel': ‘default banners 3 - desktop'})\"])[2]").click()
        # driver.find_element_by_xpath("//img[@alt='Ray-Ban RB3447 Round Metal Sunglasses']").click()
        # driver.find_element_by_xpath("//img[@alt='Oakley OO4123 HOLBROOK METAL Polarized Sunglasses']").click()
        # driver.find_element_by_xpath("(//img[@alt='Maui Jim Hookipa Polarized Sunglasses'])[2]").click()
        # driver.find_element_by_xpath("(//img[@alt='Maui Jim Hookipa Polarized Sunglasses'])[2]").click()
        # driver.find_element_by_xpath("//img[@alt='Ralph by Ralph Lauren RA7044 Eyeglasses']").click()
        # driver.find_element_by_xpath("//img[@alt='Persol PO3007V Eyeglasses']").click()
        # driver.find_element_by_link_text("Top Sunglasses").click()
        # driver.find_element_by_link_text("Top Eyeglasses").click()
        # driver.find_element_by_link_text("Top Eyeglasses").click()
        # driver.find_element_by_link_text("Help & Contact").click()
        # driver.find_element_by_link_text("FAQ").click()
        # driver.find_element_by_xpath("(//a[contains(text(),'Order Tracking')])[2]").click()
        # driver.find_element_by_xpath("(//a[contains(text(),'Shipping Information')])[2]").click()
        # driver.find_element_by_link_text("Returns & Exchanges").click()
        # driver.find_element_by_xpath("(//a[contains(text(),'HSA & FSA')])[2]").click()
        # driver.find_element_by_link_text("How to buy online").click()
        # driver.find_element_by_xpath("(//a[contains(text(),'Shopping Guides')])[3]").click()
        # driver.find_element_by_link_text("Shop by personality").click()
        # driver.find_element_by_link_text("Celebrity Spotters").click()
        # driver.find_element_by_link_text("Virtual Try-On").click()
        # driver.find_element_by_link_text("Best Price Guarantee").click()
        # driver.find_element_by_link_text("Student Discount").click()
        # driver.find_element_by_link_text("Affiliate").click()
        # driver.find_element_by_link_text("Military Discount").click()
        # driver.find_element_by_link_text("About Us").click()
        # driver.find_element_by_link_text("Authenticity").click()
        # driver.find_element_by_link_text("BUY ONE GIVE ONE").click()
        # driver.find_element_by_link_text("In The News").click()
        # driver.find_element_by_xpath("//div[@id='footer']/div/div/div[2]/ul/li[3]/a/i").click()
        # driver.find_element_by_xpath("//ul[@id='menuN_level_6']/li/div/div[2]/a/p").click()
        # driver.find_element_by_xpath("//ul[@id='menuN_level_6']/li/div/div[2]/a[2]/p").click()
        # driver.find_element_by_xpath("//ul[@id='menuN_level_6']/li/div/div[2]/a[3]/p").click()
        # driver.find_element_by_xpath("//ul[@id='menuN_level_6']/li/div/div[2]/a[4]/p").click()
        # driver.find_element_by_xpath("//ul[@id='menuN_level_6']/li/div/div[2]/a[5]/p").click()
        # driver.find_element_by_xpath(
        #     "//a[@onclick=\"promoClick();dataLayer.push({'event':'GAEvent', 'eventCategory': 'Mega Menu', 'eventAction': 'click', 'eventLabel': 'On Sale Eyeglasses Banner MM 2017'})\"]").click()
        # driver.find_element_by_xpath(
        #     "//a[@onclick=\"promoClick();dataLayer.push({'event':'GAEvent', 'eventCategory': 'Mega Menu', 'eventAction': 'click', 'eventLabel': 'On Sale Sunglasses Banner MM 2017'})\"]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def move_to(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def assertTitle(self, title):
        try:
            self.assertEqual(title, self.driver.title)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def assertText(self, how, what, text):
        try:
            self.assertEqual(text, self.driver.find_element(by=how, value=what).text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
