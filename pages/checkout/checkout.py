from selenium.webdriver.common.by import By
from util.BasePage import BasePage


class Checkout(BasePage):
    MS = (By.ID, "billing_title_2")
    MR = (By.ID, "billing_title_1")
    billing_first_name = (By.ID, "billing_first_name")
    billing_last_name = (By.ID, "billing_last_name")
    billing_email = (By.ID, "billing_email")
    billing_telephone = (By.ID, "billing_telephone")
    billing_address1 = (By.ID, "billing_address1")
    billing_address2 = (By.ID, "billing_address2")
    billing_state = (By.ID, "billing_state")
    billing_state_option = (By.XPATH, "//option[@value='Armed Forces Canada']")
    billing_city = (By.ID, "billing_city")
    billing_post_code = (By.ID, "billing_post_code")
    proceed_payment = (By.XPATH, "//button[@type='submit']")
    card_number = (By.ID, "cardNumber")
    card_expiry_month = (By.ID, "mmexpiryDate")
    card_expiry_month_value = (By.XPATH, "//select[@id='mmexpiryDate']/option[@value='02']")
    card_expiry_year = (By.ID, "yyexpiryDate")
    card_expiry_year_value = (By.XPATH, "//select[@id='yyexpiryDate']/option[@value='2020']")
    cvv = (By.ID, "cvv")
    place_order = (By.ID, "btnSubmit")

    def put_address(self):
        self.send_key(self.billing_first_name, "Sharly")
        self.send_key(self.billing_last_name, "Xing")
        self.send_key(self.billing_email, "sharly.xing@motionglobal.com")
        self.send_key(self.billing_telephone, "13517212112")
        self.send_key(self.billing_address1, "North Zhongshao Road No.470")
        self.send_key(self.billing_address2, "No.3 Tower 3F")
        self.choose_us_status()
        self.send_key(self.billing_city, "Shanghai")
        self.send_key(self.billing_post_code, "AB 3451")

    def choose_us_status(self):
        self.click(self.billing_state)
        self.click(self.billing_state_option)

    def input_card(self):
        self.send_key(self.card_number, "4111111111111111")
        self.click(self.card_expiry_month)
        self.click(self.card_expiry_month_value)
        self.click(self.card_expiry_year)
        self.click(self.card_expiry_year_value)
        self.send_key(self.cvv, '121')
