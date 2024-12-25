from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # 导入 By 类

# 指定 ChromeDriver 的路径
driverPath = r'C:\Users\kaiwu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# 创建 Service 对象
service = Service(driverPath)

# 启动 Chrome 浏览器
browser = webdriver.Chrome(service=service)

# 访问目标网页
url = 'http://www.mcut.edu.tw/?Lang=en'
browser.get(url)  # 网页下载至浏览器

# 使用 By.CLASS_NAME 查找元素
txtBox = browser.find_element(By.CLASS_NAME, 'form-control')  # 修复错误
txtBox.send_keys('王永慶')  # 输入表单数据

txtBox.submit()  # 送出表单

time.sleep(5)  # 暂停5秒
