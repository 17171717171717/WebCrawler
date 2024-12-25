# ch7_8.py
from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 指定 ChromeDriver 的路径
driverPath = r'C:\Users\kaiwu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# 创建 Service 对象
service = Service(driverPath)

# 启动 Chrome 浏览器
browser = webdriver.Chrome(service=service)
url = 'https://deepmind.com.tw'
browser.get(url)                # 網頁下載至瀏覽器

eleLink = browser.find_element_by_link_text('深智數位緣起')
print(type(eleLink))            # 列印eleLink資料類別
time.sleep(5)                   # 暫停5秒
eleLink.click()                 







