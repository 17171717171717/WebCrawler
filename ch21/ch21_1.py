from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 引入 Service 模块
from selenium.webdriver.common.by import By  # 导入 By 模块
import time

# 網址處理
url_yahoo = 'https://tw.bid.yahoo.com/search/auction/product?'
url_product = 'kw=薩爾達傳說&p=薩爾達傳說&sort=-ptime'
url = url_yahoo + url_product

# 驱动路径
driverPath = r'C:\Users\kaiwu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# 创建 Service 对象，并传入驱动路径
service = Service(driverPath)

# 使用 Service 对象初始化 Chrome 浏览器
browser = webdriver.Chrome(service=service)

browser.implicitly_wait(5)  # 等待網頁載入
browser.get(url)  # 網頁下載至瀏覽器

# 商品連結
linkPath = "//ul[@class='gridList']/li/a"
product_links = browser.find_elements(By.XPATH, linkPath)
print(product_links)
product_link = product_links[0].get_attribute('href')
print('商品連結 : ', product_link)

# 商品名稱
titlePath = "//span[contains(@class,'BaseGridItem__title___2HWui')]"
product_titles = browser.find_elements(By.XPATH, titlePath)
product_title = product_titles[0].get_attribute('textContent')
print('商品名稱 : ', product_title)

# 商品價格
pricePath = "//span[contains(@class,'BaseGridItem__price___31jkj')]/em"
product_prices = browser.find_elements(By.XPATH, pricePath)
product_price = product_prices[0].text
print('商品價格 : ', product_price)

# 等待一段时间，方便浏览器完成操作后再关闭
time.sleep(5)
browser.quit()  # 关闭浏览器
