----------------------------------------------------------
#### 关于框架：
框架基于Python3+Selenium3+Unittest搭建的WebUI自动化测试框架

#### 特点：
- 支持多种定位方式，包括（xpath/css/ID/text/link_text/name）
- 框架集成了Selenium的常用定位方法，使元素定位更加方便
- 使用HTMLTestRunner作为自动生成测试报告，报告更加美观，更加详细，内容更丰富
- Logging日志输出，可以看到每一步做的操作

#### 部署环境：
- Python 3
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
Build 之前需要新建2个文件夹

screenshots 用于存放case失败截图
logs 用于存放log


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
