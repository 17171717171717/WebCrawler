# ch7_4_1.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 指定 ChromeDriver 的路径
driverPath = r'C:\Users\kaiwu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# 创建 Service 对象
service = Service(driverPath)

# 启动 Chrome 浏览器
browser = webdriver.Chrome(service=service)

url = 'http://aaa.24ht.com.tw'
browser.get(url)                # 網頁下載至瀏覽器
print(browser.page_source)      # 列印網頁原始碼
            

