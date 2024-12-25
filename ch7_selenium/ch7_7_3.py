from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # 导入 By 类

# 指定 ChromeDriver 的路径
driverPath = r'C:\Users\kaiwu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# 创建 Service 对象
service = Service(driverPath)

# 启动 Chrome 浏览器
browser = webdriver.Chrome(service=service)

# 使用 file:// 前缀加载本地 HTML 文件
url = r'file:///C:\Users\kaiwu\OneDrive\桌面\自學\網路爬蟲\讀者資源\ch7/h7_1.html'  # 请确保路径使用正斜杠
browser.get(url)  # 网页下载至浏览器
            # 網頁下載至瀏覽器

n1 = browser.find_element_by_xpath("//section/p[1]")
print(n1.text)
n2 = browser.find_element_by_xpath("//section/p[2]")
print(n2.text)
