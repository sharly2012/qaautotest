import time
import configparser
from util.BasePage import BasePage
from selenium.webdriver.common.by import By

config = configparser.ConfigParser()
config.read("/Users/admin/PycharmProjects/sbg2018/sbg/config/config.ini")
usr = config.get("OMAccount", "username")
pwd = config.get("OMAccount", "password")


class OMPage(BasePage):
    username = (By.ID, "username")
    password = (By.ID, "password")
    verify_code = (By.XPATH, "/html/body/div/form/div/div/div[3]/input")
    verify = (By.ID, "verifyImg")
    login_button = (By.ID, "sub")
    voucher_code = (By.XPATH, "//div[@id='page']/table/tbody/tr[2]/td/table/tbody/tr[2]/td[10]/span")

    def login(self):
        for i in range(10):
            if self.driver.current_url != "http://om.motionglobal.com/index/dashboard":
                self.clear(self.username)
                self.send_key(self.username, usr)
                self.clear(self.password)
                self.send_key(self.password, pwd)
                text = self.image_to_string(self.verify)
                self.clear(self.verify_code)
                self.send_key(self.verify_code, text)
                time.sleep(1)
                try:
                    self.click(self.login_button)
                    time.sleep(2)
                    self.alert_accept()
                except Exception as e:
                    print(e)
            else:
                print("Had try %s times" % i)
                print("Login successfully")
                break

    def create_voucher(self, total_amount, current_url):
        self.login()
        # total_amount = str(100)
        date_now = (time.strftime("%d/%m/%Y"))
        # current_url = "www.visiondirect.com.au"
        url = "http://om.motionglobal.com/giftvoucher/add?amount=" + total_amount \
              + "&minimum-amount=1&quantity=1&expiry-date=" + date_now \
              + "&admin-sel=Sharly&comments=onlinetest&domains[]=" + current_url
        self.driver.get(url)
        time.sleep(1)
        voucher = self.get_attribute_text(self.voucher_code)
        return voucher
