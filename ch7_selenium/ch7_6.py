# ch7_6.py
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


try:
    tag = browser.find_element_by_id('main')
    print(tag.tag_name)
except:
    print("沒有找到相符的元素")


            

