#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest
from util.BrowserDriver import BrowserDriver
from pages.HomePage import HomePage


class Search(unittest.TestCase):

    def setUp(self):
        self.drivers = BrowserDriver()
        self.driver = self.drivers.openbrowser()

    # def login(self):
    #     homepage = HomePage(self.driver)
    #     homepage.send_key(homepage.search_box, 'Ray Ban')
    #     homepage.click(homepage.search_button)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
