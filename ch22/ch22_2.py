import requests
from bs4 import BeautifulSoup

url = "https://www.railway.gov.tw/tra-tip-web/tip/tip004/tip421/restCode?RestNo=A210"

# 发出请求并检查响应状态
response = requests.get(url)
if response.status_code == 200:
    obj = BeautifulSoup(response.text, 'lxml')

    # 查找餐厅标题
    restaurant = obj.find("h3", class_="shop-title")
    if restaurant:
        print(restaurant.text)
    else:
        print("无法找到餐厅标题")

    print("-" * 70)

    # 查找餐厅菜单
    food = obj.find("ul", class_="shop-item")
    if food:
        meals = food.find_all("li")
        for meal in meals:
            title = meal.find("div", class_="pro-title")
            if title:
                print("台中鐵路便當 :", title.text)
            else:
                print("找不到便當名称")

            price = meal.find("strong")
            if price:
                print("鐵路便當價格 :", price.text)
            else:
                print("找不到便當价格")

            print("-" * 70)
    else:
        print("无法找到菜单项")
else:
    print(f"请求失败，状态码: {response.status_code}")
