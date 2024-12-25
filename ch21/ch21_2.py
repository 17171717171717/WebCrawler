from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 引入 Service 模块
from selenium.webdriver.common.by import By  # 导入 By 模块

# 網址處理
url_yahoo = 'https://tw.bid.yahoo.com/search/auction/product?'
url_product = 'kw=薩爾達傳說&p=薩爾達傳說&sort=-ptime'
url = url_yahoo + url_product

# 擷取網頁
driverPath = r'C:\Users\kaiwu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# 创建 Service 对象，并传入 chromedriver 的路径
service = Service(driverPath)

# 使用 Service 对象初始化 Chrome 浏览器
browser = webdriver.Chrome(service=service)

browser.implicitly_wait(5)  # 等待網頁載入
browser.get(url)  # 網頁下載至瀏覽器

# 商品連結
linkPath = "//ul[@class='gridList']/li/a"
product_links = browser.find_elements(By.XPATH, linkPath)

# 商品名稱
titlePath = "//span[contains(@class,'BaseGridItem__title___2HWui')]"
product_titles = browser.find_elements(By.XPATH, titlePath)

# 商品價格
pricePath = "//span[contains(@class,'BaseGridItem__price___31jkj')]/em"
product_prices = browser.find_elements(By.XPATH, pricePath)

# 計算商品數量
num = len(product_titles)
print('商品數量 : ', num)
print('-' * 50)

# 列出商品資訊
for title, link, price in zip(product_titles, product_links, product_prices):
    print('商品名稱 : ', title.get_attribute('textContent'))
    print('商品連結 : ', link.get_attribute('href'))
    print('商品價格 : ', price.text)
    print('-' * 70)

# 停留一段时间后关闭浏览器
browser.quit()
