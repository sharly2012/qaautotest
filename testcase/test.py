#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest
from util.BrowserDriver import BrowserDriver
from pages.HomePage import HomePage


class PopClose(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.open_browser(cls)

    def setUp(self):
        pass

    def test_pop_close(self):
        homepage = HomePage(self.driver)
        homepage.close_geo_popup()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
