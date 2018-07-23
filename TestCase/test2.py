from selenium import webdriver
import unittest


class TestAAA(unittest.TestCase):

    def test_aaa(self):
        url = 'https://www.smartbuyglasses.ks'
        driver = webdriver.Chrome()
        driver.set_window_size(1440, 900)
        driver.get(url)
        # self.assertTrue(driver.title in url)
        self.assertEqual(driver.title, url[8:])


if __name__ == '__main__':
    unittest.main()
