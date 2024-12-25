# ch10_5.py
import requests, bs4
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }


url = 'https://www.chinatimes.com/world/?chdtv'
newshtml = requests.get(url, headers=headers)                 # 中國時報新聞
objSoup = bs4.BeautifulSoup(newshtml.text, 'lxml')  # 取得HTML
itemobj = objSoup.find('body')
print(itemobj)
print("----------------")
itemobj = objSoup.find('div','wrapper')
print(itemobj)
print("----------------")
itemobj = objSoup.find('div')
print(itemobj)
print("----------------")
itemobj = objSoup.find('div')
print(itemobj)
print("----------------")
itemobj = objSoup.find('div')
print(itemobj)


itemobj = objSoup.find('section', 'hot-news')
print(itemobj)
itemobj = objSoup.find('section', 'hot-news')
print(itemobj)
itemobj = itemobj.find('ol', 'vertical-list')
print(itemobj)
items = itemobj.find_all('li')
for item in items:
    txt = item.h4.text               
    print(txt)
    


    
          


                     



    
    

    





















