# ch7_4_3.py

import time

urls = ['http://aaa.24ht.com.tw',
        'http://www.mcut.edu.tw',
        'http://www.siliconstone.org']

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 指定 ChromeDriver 的路径
driverPath = r'C:\Users\kaiwu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# 创建 Service 对象
service = Service(driverPath)

# 启动 Chrome 浏览器
browser = webdriver.Chrome(service=service)

for url in urls:
    browser.get(url)                # 網頁下載至瀏覽器
    time.sleep(5)

browser.quit()






            

