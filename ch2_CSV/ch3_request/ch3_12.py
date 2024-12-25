# ch3_12.py
import requests

url = 'http://aaa.24ht.com.tw/'
response = requests.get(url)
print(response.raise_for_status())