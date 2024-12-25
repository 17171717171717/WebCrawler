import requests
from bs4 import BeautifulSoup

url_tsmc = 'https://zh.wikipedia.org/wiki/%E5%8F%B0%E7%81%A3%E7%A9%8D%E9%AB%94%E9%9B%BB%E8%B7%AF%E8%A3%BD%E9%80%A0'
tsmchtml = requests.get(url_tsmc)
objSoup = BeautifulSoup(tsmchtml.text, 'lxml')

# 查找标题
tsmc = objSoup.find('div', id='content')
if tsmc and tsmc.h1:
    print(tsmc.h1.text)  # 标题
else:
    print("未找到标题")

# 查找维基百科标识
wi = tsmc.find('div', id='siteSub') if tsmc else None
if wi:
    print(wi.text)
else:
    print("未找到维基百科标识")

# 查找主文信息
info = tsmc.find('p') if tsmc else None
if info:
    print(info.text)
else:
    print("未找到主文信息")
