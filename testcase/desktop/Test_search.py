#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest
from util.BrowserDriver import BrowserDriver
from pages.homepage.HomePage import HomePage
from util.logger import Logger

logger = Logger(logger='TestLogin').get_log()


class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.open_browser(cls)

    def setUp(self):
        pass

    def test_search(self):
        homepage = HomePage(self.driver)
        homepage.close_geo_popup()
        homepage.close_newsletter_popup()
        homepage.send_key(homepage.search_box, 'Ray Ban')
        homepage.click(homepage.search_button)
        try:
            self.assertIn("Ray Ban", homepage.get_attribute_text(homepage.search_result))
            logger.info("*************************************************************")
            logger.info("result view correct")
        except Exception as e:
            logger.info("*************************************************************")
            logger.info("search result is not correct:", format(e))
            raise

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
