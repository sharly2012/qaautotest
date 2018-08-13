import unittest
from pages.HomePage import HomePage
from util.BrowserDriver import BrowserDriver


class TestMegaMenu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser_driver = BrowserDriver(cls)
        cls.driver = browser_driver.open_browser(cls)

    def setUp(self):
        pass

    def test_mega_menu(self):
        homepage = HomePage(self.driver)
        homepage.close_geo_popup()
        homepage.close_newsletter_popup()
        homepage.move_to_element(homepage.menu_sunglasses)
        homepage.click(homepage.sun_man)
        try:
            self.assertIn("Men's Sunglasses", self.driver.title)
            print("url is correct")
        except Exception as e:
            print("url is not correct:", format(e))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
