from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # 导入 By 类

# 指定 ChromeDriver 的路径
driverPath = r'C:\Users\kaiwu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'  # 使用原始字符串或双反斜杠

# 设置 ChromeOptions 为无头模式
headless_options = webdriver.ChromeOptions()
headless_options.add_argument('--headless')  # 隐藏浏览器界面

# 创建 Service 对象
service = Service(driverPath)

# 启动 Chrome 浏览器
browser = webdriver.Chrome(service=service, options=headless_options)

# 使用 file:// 前缀加载本地 HTML 文件
url =r'file:///C:\Users\kaiwu\OneDrive\桌面\自學\網路爬蟲\讀者資源\h7_4.html'  # 确保路径格式正确
browser.implicitly_wait(5)  # 等待网页载入
browser.get(url)  # 网页下载至浏览器

# 使用新的查找方式定位元素
n = browser.find_element(By.XPATH, "//div[@id='Traveling']//a[contains(text(),'深智')]")

# 输出元素的 outerHTML 和 href 属性
print(n.get_attribute('outerHTML'))
print(n.get_attribute('href'))

# 关闭浏览器
# browser.quit()
