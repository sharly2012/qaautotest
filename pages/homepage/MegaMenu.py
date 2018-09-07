from selenium.webdriver.common.by import By
from util.BasePage import BasePage


class MegaMenu(BasePage):
    menu_sunglasses = (By.ID, 'menuN_1')
    menu_eyeglasses = (By.ID, 'menuN_2')
    menu_CL = (By.ID, 'menuN_5')
    menu_our_collection = (By.ID, 'menuN_8')
    menu_explore = (By.ID, 'menuN_6')
    menu_deals = (By.ID, 'menuN_7')

