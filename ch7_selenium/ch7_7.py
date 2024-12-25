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


print("網頁標題內容是 = ", browser.title)

tag2 = browser.find_element_by_id('author')             # 傳回<h1>
print("\n標籤名稱 = %s, 內容是 = %s " % (tag2.tag_name, tag2.text))

print()
tag3 = browser.find_elements_by_id('content')           # 傳回<h1>
for t3 in tag3:
    print("標籤名稱 = %s, 內容是 = %s " % (t3.tag_name, t3.text))

print()
tag4 = browser.find_elements_by_tag_name('p')           # 傳回<p>
for t4 in tag4:
    print("標籤名稱 = %s, 內容是 = %s " % (t4.tag_name, t4.text))

print()
tag5 = browser.find_elements_by_tag_name('img')         # 傳回<img>
for t5 in tag5:
    print("標籤名稱 = %s, 內容是 = %s " % (t5.tag_name, t5.get_attribute('src')))
