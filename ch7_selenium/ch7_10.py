from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # 导入 By 类
driverPath = r'C:\Users\kaiwu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# 创建 Service 对象
service = Service(driverPath)

# 启动 Chrome 浏览器
browser = webdriver.Chrome(service=service)
url = 'http://www.mcut.edu.tw'
browser.get(url)                    # 网页下载至浏览器

# 使用 By.TAG_NAME 查找 body 元素
ele = browser.find_element(By.TAG_NAME, 'body')

time.sleep(3)
print(1)

# 使用 Keys 模拟按键操作，滚动网页
ele.send_keys(Keys.PAGE_DOWN)       # 网页向下滚动一页
time.sleep(3)
print(2)

ele.send_keys(Keys.END)             # 网页滚动到底部
time.sleep(3)
print(3)

ele.send_keys(Keys.PAGE_UP)         # 网页向上滚动一页
time.sleep(3)
print(4)

ele.send_keys(Keys.HOME)            # 网页滚动到顶部

# 关闭浏览器
browser.quit()
