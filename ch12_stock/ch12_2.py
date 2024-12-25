from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 引入 Service 模块
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # 导入 By 模块
import time

url = 'https://www.tpex.org.tw/web/stock/aftertrading/daily_trading_info/st43.php?l=zh-tw'

# 驱动路径
driverPath = r'C:\Users\kaiwu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# 创建 Service 对象，并传入驱动路径
service = Service(driverPath)

# 使用 Service 对象初始化 Chrome 浏览器
browser = webdriver.Chrome(service=service)

# 打开目标网址
browser.get(url)

# 找到股票代码输入框，并输入代码
text_stock = browser.find_element(By.ID, 'input_stock_code')  # 使用新的查找方法
print(text_stock)
text_stock.send_keys('5351')  # 设置股票代码
text_stock.send_keys(Keys.ENTER)  # 模拟按下回车键
time.sleep(3)  # 等待页面加载

# 找到下载CSV按钮，并点击下载
btn = browser.find_elements(By.CLASS_NAME, 'download-csv')  # 使用新的查找方法
print(btn)
btn[1].click()  # 点击第二个按钮
time.sleep(3)  # 等待下载完成


