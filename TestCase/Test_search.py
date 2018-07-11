#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest
from util.BrowserDriver import BrowserDriver
from pages.HomePage import HomePage


class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.open_browser(cls)

    def setUp(self):
        pass

    def test_search(self):
        homepage = HomePage(self.driver)
        homepage.send_key(homepage.search_box, 'Ray Ban')
        homepage.click(homepage.search_button)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
