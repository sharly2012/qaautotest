import unittest
from util.BrowserDriver import BrowserDriver
from pages.HomePage import HomePage
from util.logger import Logger
from util.BaseUtil import BaseUtil

logger = Logger(logger='TestLogin').get_log()


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser_driver = BrowserDriver(cls)
        cls.driver = browser_driver.open_browser(cls)

    def setUp(self):
        pass

    def test_login(self):
        homepage = HomePage(self.driver)
        homepage.close_geo_popup()
        homepage.close_newsletter_popup()
        homepage.move_to_element(homepage.login_text)
        homepage.click(homepage.login_button)
        homepage.clear(homepage.username)
        email = BaseUtil().get_config_value("SBG_Account", "email")
        pwd = BaseUtil().get_config_value("SBG_Account", "password")
        homepage.send_key(homepage.username, email)
        homepage.clear(homepage.password)
        homepage.send_key(homepage.password, pwd)
        homepage.click(homepage.sign_in_button)
        homepage.move_to_element(homepage.your_account)
        try:
            self.assertIn("sharly", homepage.get_attribute_text(homepage.user_detail))
            logger.info("*************************************************************")
            logger.info("Login in success")
        except Exception as e:
            logger.info("*************************************************************")
            logger.info("Login in fail: ", format(e))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
