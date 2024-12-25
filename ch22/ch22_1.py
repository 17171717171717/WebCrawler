from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 引入 Service 模块
from selenium.webdriver.common.by import By  # 导入 By 模块
from selenium.webdriver.support.ui import WebDriverWait  # 引入 WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # 引入显式等待条件

url = "https://rent.housefun.com.tw/region/台北市/?cid=0000"

# 擷取網頁
driverPath = r'C:\Users\kaiwu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# 创建 Service 对象，并传入 chromedriver 的路径
service = Service(driverPath)

# 使用 Service 对象初始化 Chrome 浏览器
browser = webdriver.Chrome(service=service)

# 使用显式等待，等待页面加载关键元素
browser.implicitly_wait(5)
browser.get(url)

try:
    # 等待页面内容加载完毕，直到目标元素出现
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "SearchContent")))

    # 使用 BeautifulSoup 解析页面源代码
    obj = BeautifulSoup(browser.page_source, "lxml")
    houseobj = obj.find("div", id="SearchContent")
    houses = houseobj.find_all("article")

    # 提取并打印房源信息
    for house in houses:
        title = house.find("h3", class_="title").find("a")
        if title:
            print("標題 : ", title.text)

        address = house.find("address", class_="addr")
        if address:
            print("地址 : ", address.text.strip())

        level = house.find("span", class_="level")
        if level:
            print("樓層 : ", level.text)

        pattern = house.find("span", class_="pattern")
        if pattern:
            print("房型 : ", pattern.text)

        price = house.find("span", class_="infos")
        if price:
            print("租金 : ", price.text)

        print("-" * 70)
    
    while(1):
        pass

finally:
    # 关闭浏览器
    browser.quit()
