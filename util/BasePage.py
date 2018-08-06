#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pytesseract
import os
import time
import cv2
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from util.logger import Logger
from PIL import Image

logger = Logger(logger='BasePage').getlog()


class BasePage(object):
    path = os.path.dirname(os.getcwd())

    def __init__(self, driver):
        """
        :param driver:打开浏览器驱动
        """
        self.driver = driver

    def get_page_title(self):
        logger.info("当前页面的title为: %s" % self.driver.title)
        return self.driver.title

    def find_element(self, *locator):
        try:
            # 元素可见时，返回查找到的元素；以下入参为元组的元素，需要加*
            WebDriverWait(self.driver, 30, 0.5).until(lambda driver: driver.find_element(*locator).is_displayed())
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            logger.warning('Can not find element: %s' % locator[1])
            raise
        except TimeoutException:
            logger.warning('Can not find element: %s' % locator[1])

    def get_screent_img(self):
        """将页面截图下来"""
        file_path = os.path.dirname(os.path.abspath('')) + '/screenshots/'
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        screen_name = file_path + now + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("页面已截图，截图的路径在项目: /screenshots路径下")
        except NameError as ne:
            logger.error("失败截图 %s" % ne)
            self.get_screent_img()

    def click(self, locator):
        logger.info('Click element by %s: %s...' % (locator[0], locator[1]))
        try:
            self.find_element(*locator).click()
            # time.sleep(1)
        except AttributeError as e:
            logger.error("无法点击元素: %s" % e)

    def clear(self, locator):
        """输入文本框清空操作"""
        element = self.find_element(*locator)
        try:
            element.clear()
            logger.info('清空文本框内容')
        except NameError as ne:
            logger.error("Failed to clear in input box with %s" % ne)
            self.get_screent_img()

    def send_key(self, locator, text):
        logger.info('Clear input-box: %s...' % locator[1])
        self.find_element(*locator).clear()
        # time.sleep(1)
        logger.info('Input element by %s: %s...' % (locator[0], locator[1]))
        logger.info('Input: %s' % text)
        try:
            self.find_element(*locator).send_keys(text)
            # time.sleep(1)
        except Exception as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_screent_img()

    def move_to_element(self, locator):
        """
        鼠标悬停操作
        Usage:
        element = ("id","xxx")
        driver.move_to_element(element)
        """
        element = self.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def back(self):
        """
        浏览器返回窗口
        """
        self.driver.back()
        logger.info('返回上一个页面')

    def forward(self):
        """
        浏览器前进下一个窗口
        """
        self.driver.forward()
        logger.info('前进到下一个页面')

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("等待 %d 秒" % seconds)

    def close(self):
        """
        关闭浏览器
        """
        try:
            self.driver.close()
            logger.info('关闭浏览器窗口')
        except NameError as ne:
            logger.error("关闭浏览器窗口失败 %s" % ne)

    def quit(self):
        """
        退出浏览器
        """
        self.driver.quit()

    def get_title(self):
        """获取title"""
        return self.driver.title

    def get_url(self):
        """获取当前的url"""
        return self.driver.current_url

    def get_text(self, locator):
        """获取文本"""
        element = self.find_element(*locator)
        return element.text

    def get_attribute(self, locator, name):
        """获取属性"""
        element = self.find_element(*locator)
        return element.get_attribute(name)

    def js_execute(self, js):
        """执行js"""
        return self.driver.execute_script(js)

    def js_focus_element(self, locator):
        """聚焦元素"""
        target = self.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        """滚动到底部"""
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def select_by_index(self, locator, index):
        """通过索引,index是索引第几个，从0开始"""
        element = self.find_element(*locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        """通过value属性"""
        element = self.find_element(*locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        """通过文本值定位"""
        element = self.find_element(*locator)
        Select(element).select_by_value(text)

    def is_text_in_element(self, locator, text, timeout=10):
        """判断文本在元素里，没定位到元素返回False，定位到元素返回判断结果布尔值"""
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(
                EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            print("元素没有定位到:" + str(locator))
            return False
        else:
            return result

    def is_text_in_value(self, locator, value, timeout=10):
        """
        判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        result = driver.text_in_element(element, text)
        """
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(
                EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            print("元素没定位到：" + str(locator))
            return False
        else:
            return result

    def is_title(self, title, timeout=10):
        """判断title完全等于"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        """判断title包含"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))
        return result

    def is_selected(self, locator, timeout=10):
        """判断元素被选中，返回布尔值,"""
        result = WebDriverWait(self.driver, timeout, 1).until(
            EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self, locator, selected=True, timeout=10):
        """判断元素的状态，selected是期望的参数true/False
        返回布尔值"""
        result = WebDriverWait(self.driver, timeout, 1).until(
            EC.element_located_selection_state_to_be(locator, selected))
        return result

    def is_alert_present(self, timeout=10):
        """判断页面是否有alert，
        有返回alert(注意这里是返回alert,不是True)
        没有返回False"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.alert_is_present())
        return result

    def alert_accept(self):
        """接受alert"""
        try:
            alert = self.driver.switch_to_alert()
            logger.info(alert.text)
            alert.accept()
        except UnexpectedAlertPresentException as e:
            print(e)
        except NoAlertPresentException as e1:
            print(e1)

    def is_visibility(self, locator, timeout=10):
        try:
            """元素可见返回本身，不可见返回Fasle"""
            result = WebDriverWait(self.driver, timeout, 1).until(
                EC.visibility_of_element_located(locator))
            return result
        except TimeoutException as e:
            logger.info(e)

    def is_invisibility(self, locator, timeout=10):
        """元素可见返回本身，不可见返回True，没找到元素也返回True"""
        result = WebDriverWait(self.driver, timeout, 1).until(
            EC.visibility_of_element_located(locator))
        return result

    def is_clickable(self, locator, timeout=10):
        """元素可以点击is_enabled返回本身，不可点击返回Fasle"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self, locator, timeout=10):
        """判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回False"""
        result = WebDriverWait(self.driver, timeout, 1).until(
            EC.presence_of_element_located(locator))
        return result

    def set_element_wait(self, wait_time, locator):
        WebDriverWait(self.driver, wait_time, 1).until(EC.presence_of_element_located(locator))

    def upload_file(self, locator, file_path):
        """上传文件"""
        try:
            self.find_element(*locator).send_keys(file_path)
            time.sleep(1)
        except Exception as e:
            logger.error("Failed to upload file %s" % e)
            self.get_screent_img()

    def switch_handle(self, title_name):
        """根据窗口title切换窗口"""
        all_Handles = self.driver.window_handles()
        for handle in all_Handles:
            if self.driver.title.find(title_name) == -1:
                self.driver.switch_to_window(handle)
            else:
                print("Can't find the handle")

    def close_geo_popup(self):
        try:
            geo_location_close = (By.XPATH, '//div[@id="wrapper"]/div[7]/div[2]/a')
            WebDriverWait(self.driver, 10, 1).until(
                EC.element_to_be_clickable(geo_location_close))
            self.click(geo_location_close)
        except Exception as e:
            logger.error("Not found GEO pop-up. ---%s" % e)

    def close_newsletter_popup(self):
        try:
            newsletter_popup_close = (By.CSS_SELECTOR,
                                      'EDM-popUp > div.EDM-popUp-box > div > a.EDM-popUp-close.close_btn')
            self.click(newsletter_popup_close)
        except Exception as e:
            logger.error("Not found newsletter pop-up. ---%s" % e)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            logger.error("Element is not present. %s" % e)
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def get_attribute_text(self, locator):
        try:
            text_content = self.find_element(*locator).get_attribute('textContent')
        except Exception as e:
            logger.error("Failed to upload file %s" % e)
            self.get_screent_img()
        return text_content

    def _get_dynamic_binary_image(self, file_dir, file_name):
        filename = self.path + '/out_img/' + file_name.split('.')[0] + '-binary.jpg'
        img_name = file_dir + '/' + file_name
        print(img_name)
        img = cv2.imread(img_name)
        # 灰值化
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 二值化
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
        cv2.imwrite(filename, img)
        return img

    # 去除边框
    def clear_border(self, img, img_name):
        filename = self.path + '/out_img/' + img_name.split('.')[0] + '-clearBorder.jpg'
        h, w = img.shape[:2]
        for y in range(0, w):
            for x in range(0, h):
                if y < 2 or y > w - 2:
                    img[x, y] = 255
                if x < 2 or x > h - 2:
                    img[x, y] = 255

        cv2.imwrite(filename, img)
        return img

    # 干扰线降噪
    def interference_line(self, img, img_name):
        filename = self.path + '/out_img/' + img_name.split('.')[0] + '-interferenceline.jpg'
        h, w = img.shape[:2]
        # ！！！opencv矩阵点是反的
        # img[1,2] 1:图片的高度，2：图片的宽度
        for y in range(1, w - 1):
            for x in range(1, h - 1):
                count = 0
                if img[x, y - 1] > 245:
                    count = count + 1
                if img[x, y + 1] > 245:
                    count = count + 1
                if img[x - 1, y] > 245:
                    count = count + 1
                if img[x + 1, y] > 245:
                    count = count + 1
                if count > 2:
                    img[x, y] = 255
        cv2.imwrite(filename, img)
        return img

    # 点降噪
    def interference_point(self, img, img_name, x=0, y=0):
        """
        9邻域框,以当前点为中心的田字框,黑点个数
        :param x:
        :param y:
        :return:
        """
        filename = self.path + '/out_img/' + img_name.split('.')[0] + '-interferencePoint.jpg'
        # 判断图片的长宽度下限
        cur_pixel = img[x, y]  # 当前像素点的值
        height, width = img.shape[:2]

        for y in range(0, width - 1):
            for x in range(0, height - 1):
                if y == 0:  # 第一行
                    if x == 0:  # 左上顶点,4邻域
                        # 中心点旁边3个点
                        sum = int(cur_pixel) \
                              + int(img[x, y + 1]) \
                              + int(img[x + 1, y]) \
                              + int(img[x + 1, y + 1])
                        if sum <= 2 * 245:
                            img[x, y] = 0
                    elif x == height - 1:  # 右上顶点
                        sum = int(cur_pixel) \
                              + int(img[x, y + 1]) \
                              + int(img[x - 1, y]) \
                              + int(img[x - 1, y + 1])
                        if sum <= 2 * 245:
                            img[x, y] = 0
                    else:  # 最上非顶点,6邻域
                        sum = int(img[x - 1, y]) \
                              + int(img[x - 1, y + 1]) \
                              + int(cur_pixel) \
                              + int(img[x, y + 1]) \
                              + int(img[x + 1, y]) \
                              + int(img[x + 1, y + 1])
                        if sum <= 3 * 245:
                            img[x, y] = 0
                elif y == width - 1:  # 最下面一行
                    if x == 0:  # 左下顶点
                        # 中心点旁边3个点
                        sum = int(cur_pixel) \
                              + int(img[x + 1, y]) \
                              + int(img[x + 1, y - 1]) \
                              + int(img[x, y - 1])
                        if sum <= 2 * 245:
                            img[x, y] = 0
                    elif x == height - 1:  # 右下顶点
                        sum = int(cur_pixel) \
                              + int(img[x, y - 1]) \
                              + int(img[x - 1, y]) \
                              + int(img[x - 1, y - 1])

                        if sum <= 2 * 245:
                            img[x, y] = 0
                    else:  # 最下非顶点,6邻域
                        sum = int(cur_pixel) \
                              + int(img[x - 1, y]) \
                              + int(img[x + 1, y]) \
                              + int(img[x, y - 1]) \
                              + int(img[x - 1, y - 1]) \
                              + int(img[x + 1, y - 1])
                        if sum <= 3 * 245:
                            img[x, y] = 0
                else:  # y不在边界
                    if x == 0:  # 左边非顶点
                        sum = int(img[x, y - 1]) \
                              + int(cur_pixel) \
                              + int(img[x, y + 1]) \
                              + int(img[x + 1, y - 1]) \
                              + int(img[x + 1, y]) \
                              + int(img[x + 1, y + 1])

                        if sum <= 3 * 245:
                            img[x, y] = 0
                    elif x == height - 1:  # 右边非顶点
                        sum = int(img[x, y - 1]) \
                              + int(cur_pixel) \
                              + int(img[x, y + 1]) \
                              + int(img[x - 1, y - 1]) \
                              + int(img[x - 1, y]) \
                              + int(img[x - 1, y + 1])

                        if sum <= 3 * 245:
                            img[x, y] = 0
                    else:  # 具备9领域条件的
                        sum = int(img[x - 1, y - 1]) \
                              + int(img[x - 1, y]) \
                              + int(img[x - 1, y + 1]) \
                              + int(img[x, y - 1]) \
                              + int(cur_pixel) \
                              + int(img[x, y + 1]) \
                              + int(img[x + 1, y - 1]) \
                              + int(img[x + 1, y]) \
                              + int(img[x + 1, y + 1])
                        if sum <= 4 * 245:
                            img[x, y] = 0
        cv2.imwrite(filename, img)
        return img

    def image_to_string(self, locator):
        # 截取当前网页，该网页有我们需要的验证码
        self.driver.save_screenshot(self.path + "/screenshots/" + "All.png")
        img_element = self.find_element(*locator)
        # 获取验证码x,y轴坐标
        location = img_element.location
        # 获取验证码的长宽
        size = img_element.size
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  # 写成我们需要截取的位置坐标
                  int(location['y'] + size['height']))
        i = Image.open(self.path + "/screenshots/" + "All.png")
        # 使用Image的crop函数，从截图中再次截取我们需要的区域
        result = i.crop(rangle)
        result.save(self.path + "/screenshots/" + "result.png")
        rgb_im = result.convert('RGB')
        rgb_im.save(self.path + "/screenshots/" + "result.jpg")
        img = Image.open(self.path + "/screenshots/" + "result.jpg")
        img.convert("L")
        # file_dir = self.path + '/screenshots'
        # img_name = "result.jpg"
        # img = self._get_dynamic_binary_image(file_dir, img_name)
        # img = self.clear_border(img, img_name)
        # img = self.interference_line(img, img_name)
        # img = self.interference_point(img, img_name)
        verify_code = pytesseract.image_to_string(img).strip()
        logger.info("verify code is: " + verify_code)
        return verify_code
