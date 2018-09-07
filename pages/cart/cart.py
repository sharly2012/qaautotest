from selenium.webdriver.common.by import By
from util.BasePage import BasePage


class Cart(BasePage):
    ingenico_checkout = (By.XPATH, "(//button[@type='button'])[3]")
    promo_code_radio = (By.XPATH, "//li[@id='voucher-code-container']/label")
    promo_code_input = (By.ID, "promo-code")
    promo_code_button = (By.XPATH, "//li[@id='voucher-code-container']/div/a")
    total_amount = (By.ID, "totalAmount")

    def get_total_amount(self):
        total_price = self.get_attribute_text(self.total_amount)
        return total_price

    def input_voucher(self, gift_voucher):
        self.click(self.promo_code_radio)
        self.send_key(self.promo_code_input, gift_voucher)
        self.click(self.promo_code_button)