from selenium.webdriver.common.by import By
from util.BasePage import BasePage


class SunProduct(BasePage):
    buy_now = (By.XPATH, '/html/body/div[1]/div[4]/div[1]/div[2]/div[5]/a[1]')
    buy_with_lens = (By.XPATH, '/html/body/div[1]/div[4]/div[1]/div[2]/div[5]/a[2]')
