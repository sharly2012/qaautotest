import os
from selenium import webdriver
from time import sleep
from threading import Thread


def test_baidu_search(browser, url):
    file_path = os.path.dirname(os.getcwd())
    chrome_driver_path = file_path + '/driver/MacOS/chromedriver'
    driver = None
    # 你可以自定义这里，添加更多浏览器支持进来
    if browser == "Safari":
        driver = webdriver.Safari()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome(chrome_driver_path)

    if driver is None:
        exit()

    driver.set_window_size(1440, 900)
    print("开始[case_0001]百度搜索")
    driver.get(url)

    print("清除搜索中数据，输入搜索关键词")
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys(u"开源优测")

    print("单击 百度一下 按钮 开始搜索")
    driver.find_element_by_id("su").click()
    sleep(3)

    print("关闭浏览器，退出webdriver")
    driver.quit()


if __name__ == "__main__":
    # 浏览器和首页url
    data = {
        "Safari": "http://www.baidu.com",
        "firefox": "http://www.baidu.com",
        "chrome": "http://www.baidu.com"
    }

    # 构建线程
    threads = []
    for b, url in data.items():
        t = Thread(target=test_baidu_search, args=(b, url))
        threads.append(t)

        # 启动所有线程
    for thr in threads:
        thr.start()
