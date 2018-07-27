import unittest
import time
from util.BrowserDriver import BrowserDriver
from pages.HomePage import HomePage
from pages.sun_product import SunProduct
from pages.cart import Cart
from pages.checkout import Checkout


class TestPayment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.open_browser(cls)

    def setUp(self):
        pass

    def test_ingenico(self):
        homepage = HomePage(self.driver)
        homepage.click(homepage.top_sellers_sun_1)
        sunproduct = SunProduct(self.driver)
        sunproduct.click(sunproduct.buy_now)
        cart = Cart(self.driver)
        cart.click(cart.promo_code_radio)
        cart.send_key(cart.promo_code_input, "GIVEME10")
        cart.click(cart.promo_code_button)
        time.sleep(1)
        cart.click(cart.ingenico_checkout)
        checkout = Checkout(self.driver)
        checkout.click(checkout.MR)
        checkout.send_key(checkout.billing_first_name, "Sharly")
        checkout.send_key(checkout.billing_last_name, "Xing")
        checkout.send_key(checkout.billing_email, "sharly.xing@motionglobal.com")
        checkout.send_key(checkout.billing_telephone, "13517212112")
        checkout.send_key(checkout.billing_address1, "North Zhongshao Road No.470")
        checkout.send_key(checkout.billing_address2, "No.3 Tower 3F")
        checkout.choose_us_status()
        checkout.send_key(checkout.billing_city, "Shanghai")
        checkout.send_key(checkout.billing_post_code, "AB 3451")
        checkout.click(checkout.proceed_payment)
        checkout.input_card()
        checkout.click(checkout.place_order)

    def test_PayPal(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass


if __name__ == "__main__":
    unittest.main()
