import unittest
from util.BrowserDriver import BrowserDriver
from pages.OMPage import OMPage


class OmTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.open_browser(cls)
        cls.driver.get("http://om.motionglobal.com")

    def setUp(self):
        pass

    # def test_login(self):
    #     om_page = OMPage(self.driver)
    #     om_page.login()

    def test_voucher(self):
        om_page = OMPage(self.driver)
        voucher = om_page.create_voucher("100", "www.visiondirect.com.au")
        print(voucher)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
