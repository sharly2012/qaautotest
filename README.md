----------------------------------------------------------
#### 关于框架：

本框架基于Python3+Selenium+Unittest搭建的WebUI自动化测试框架

#### 特点：

- 框架集成了Selenium的常用定位方法，使元素定位更加方便
- 使用PageObject，维护更加方便
- 使用HTMLTestRunner作为自动生成测试报告，报告更加美观，更加详细，内容更丰富
- Logging日志输出，可以看到每一步做的操作
- 失败会截图保存到screenshots目录下，更方便查找问题


#### 部署环境：
- Python 3
- pip3

#### 使用到的package：

> pip3 install selenium

> pip3 install PyYAML

> pip3 install openpyxl

> pip3 install pycparser

> pip3 install PyMySQL

> pip3 install configparser

> pip3 install pytesseract

> pip3 install Pillow

> pip3 install opencv-python

####
修改/util/BaseUtil.py中root_path路径为当前项目的主目录


#### 支持的浏览器及驱动：
基于Selenium支持的所有浏览器

browser == "Chrome"
browser == "Firefox"
browser == "IE"
browser == "Safari"
browser == "Opera"
browser == "Edge"


#### 浏览器及驱动下载地址：
geckodriver(Firefox):https://github.com/mozilla/geckodriver/releases

Chromedriver(Chrome):https://sites.google.com/a/chromium.org/chromedriver/home

IEDriverServer(IE):http://selenium-release.storage.googleapis.com/index.html

operadriver(Opera):https://github.com/operasoftware/operachromiumdriver/releases

MicrosoftWebDriver(Edge):https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver
