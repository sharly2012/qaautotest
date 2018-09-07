import unittest
import time
from util.BrowserDriver import BrowserDriver
from pages.homepage.HomePage import HomePage
from pages.product.sun_product import SunProduct
from pages.cart.cart import Cart
from pages.checkout.checkout import Checkout
from pages.OMPage import OMPage


class TestPayment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.open_browser(cls)

    def setUp(self):
        pass

    def test_ingenico(self):
        url = self.driver.current_url[9:].split("/")[0]
        homepage = HomePage(self.driver)
        if homepage.is_visibility(homepage.geo_cnt):
            homepage.click(homepage.geo_close_btn)
        else:
            pass

        if homepage.is_visibility(homepage.EDM_popUp_cnt):
            homepage.click(homepage.EDM_popUp_close_btn)
        else:
            pass
        homepage.click(homepage.top_sellers_sun_1)
        sunproduct = SunProduct(self.driver)
        sunproduct.click(sunproduct.buy_now)
        cart = Cart(self.driver)
        cart.click(cart.promo_code_radio)
        total_price = cart.get_total_amount()
        voucher = total_price[1:].split(".")[0]
        price = str(int(int(voucher)*0.99))
        new_window = "window.open('http://om.motionglobal.com');"
        self.driver.execute_script(new_window)
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
        om_page = OMPage(self.driver)
        gift_voucher = om_page.create_voucher(price, url)
        self.driver.switch_to_window(handles[0])
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
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
