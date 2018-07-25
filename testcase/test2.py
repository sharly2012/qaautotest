import pytesseract
import os
from PIL import Image

path = os.path.dirname(os.getcwd())
img = Image.open(path + "/screenshots/" + "result.png")  # 先创建image对象
text = pytesseract.image_to_string(img).strip()  # 直接转化成string，更多参数可以查看文档
print(text)

