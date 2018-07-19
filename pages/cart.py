from selenium.webdriver.common.by import By
from util.BasePage import BasePage


class Cart(BasePage):
    ingenico_checkout = (By.XPATH, "(//button[@type='button'])[3]")
