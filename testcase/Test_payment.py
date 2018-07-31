import unittest
import time
from util.BrowserDriver import BrowserDriver
from pages.HomePage import HomePage
from pages.sun_product import SunProduct
from pages.cart import Cart
from pages.checkout import Checkout
from pages.OMPage import OMPage


class TestPayment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.open_browser(cls)

    def setUp(self):
        pass

    def test_ingenico(self):
        url = self.driver.current_url
        homepage = HomePage(self.driver)
        homepage.click(homepage.top_sellers_sun_1)
        sunproduct = SunProduct(self.driver)
        sunproduct.click(sunproduct.buy_now)
        cart = Cart(self.driver)
        cart.click(cart.promo_code_radio)
        om_page = OMPage(self.driver)
        gift_voucher = om_page.create_voucher()
        cart.send_key(cart.promo_code_input, gift_voucher)
        cart.click(cart.promo_code_button)
        time.sleep(1)
        cart.click(cart.ingenico_checkout)
        checkout = Checkout(self.driver)
        checkout.click(checkout.MR)
        checkout.put_address()
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
