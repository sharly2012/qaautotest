import unittest
from util.BrowserDriver import BrowserDriver
from pages.HomePage import HomePage


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.open_browser(cls)

    def setUp(self):
        pass

    def test_login(self):
        homepage = HomePage(self.driver)
        homepage.close_geo_popup()
        homepage.close_newsletter_popup()
        homepage.move_to_element(homepage.login_text)
        homepage.click(homepage.login_button)
        homepage.clear(homepage.username)
        email = homepage.get_config_value("SBG_Account", "email")
        pwd = homepage.get_config_value("SBG_Account", "password")
        homepage.send_key(homepage.username, email)
        homepage.clear(homepage.password)
        homepage.send_key(homepage.password, pwd)
        homepage.click(homepage.sign_in_button)
        
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
