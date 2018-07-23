#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "https://www.smartbuyglasses.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.smartbuyglasses.com/")
        driver.find_element_by_xpath("//ul[@id='pro_slider_sunglasses']/li/a").click()
        driver.find_element_by_xpath(
            "(//a[@onclick='addEventTrack(\"GAEvent\", \"Product Page v2\", \"click\", \"Select other size\")'])[2]").click()
        driver.find_element_by_xpath("//div[@id='suspend_product_image']/div[2]/div[5]/a/span").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_id("billing_first_name").clear()
        driver.find_element_by_id("billing_first_name").send_keys("Sharly")
        driver.find_element_by_id("billing_last_name").clear()
        driver.find_element_by_id("billing_last_name").send_keys("Xing")
        driver.find_element_by_id("billing_email").clear()
        driver.find_element_by_id("billing_email").send_keys("sharly.xing@motionglobal.com")
        driver.find_element_by_id("billing_telephone").clear()
        driver.find_element_by_id("billing_telephone").send_keys("13817261234")
        driver.find_element_by_id("billing_address1").clear()
        driver.find_element_by_id("billing_address1").send_keys("North Zhongshan Road NO.470")
        driver.find_element_by_id("billing_address2").clear()
        driver.find_element_by_id("billing_address2").send_keys("address 2")
        driver.find_element_by_id("billing_state").click()
        Select(driver.find_element_by_id("billing_state")).select_by_visible_text("Armed Forces Canada")
        driver.find_element_by_xpath("//option[@value='Armed Forces Canada']").click()
        driver.find_element_by_id("billing_city").clear()
        driver.find_element_by_id("billing_city").send_keys("Shanghai")
        driver.find_element_by_id("billing_post_code").clear()
        driver.find_element_by_id("billing_post_code").send_keys("200120")
        driver.find_element_by_xpath("//button[@type='submit']").click()

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
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
