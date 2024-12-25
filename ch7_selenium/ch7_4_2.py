# ch7_4_2.py
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
print('瀏覽器名稱 = ', browser.name)             # 列印瀏覽器名稱
print('網頁url    = ', browser.current_url)      # 列印網頁url
print('網頁連線id = ', browser.session_id)       # 網頁連線id
print('瀏覽器功能 = \n',browser.capabilities)    # 瀏覽器功能設定訊息



            

