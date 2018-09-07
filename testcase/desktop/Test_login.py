import unittest
import paramunittest
from util.BrowserDriver import BrowserDriver
from pages.homepage.HomePage import HomePage
from util.logger import Logger

logger = Logger(logger='TestLogin').get_log()


@paramunittest.parametrized({"email": "", "password": ""},
                            {"email": "admin", "password": ""},
                            {"email": "", "password": "12121"},
                            {"email": "sharly.xing@motionglobal.com", "password": "1qaz@WSX"})
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser_driver = BrowserDriver(cls)
        cls.driver = browser_driver.open_browser(cls)

    def setUp(self):
        pass

    def setParameters(self, email, password):
        self.email = email
        self.password = password

    def test_login(self):
        homepage = HomePage(self.driver)
        homepage.close_geo_popup()
        homepage.close_newsletter_popup()
        homepage.move_to_element(homepage.login_text)
        homepage.click(homepage.login_button)
        homepage.clear(homepage.username)
        # email = BaseUtil().get_config_value("SBG_Account", "email")
        # pwd = BaseUtil().get_config_value("SBG_Account", "password")
        homepage.send_key(homepage.username, self.email)
        homepage.clear(homepage.password)
        homepage.send_key(homepage.password, self.password)
        homepage.click(homepage.sign_in_button)
        homepage.move_to_element(homepage.your_account)
        try:
            self.assertIn("sharly", homepage.get_attribute_text(homepage.user_detail))
            logger.info("*************************************************************")
            logger.info("Login in success")
        except Exception as e:
            logger.info("*************************************************************")
            logger.info("Login in fail: ", format(e))
            homepage.get_screent_img()
            raise

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
