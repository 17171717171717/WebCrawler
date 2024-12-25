# ch3_32.py
import requests, json

url = 'https://www.httpbin.org/post'
form_data = {'gender':'M','page':'1'}
print(type(form_data))
print(type(json.dumps(form_data)))
print(json.dumps(form_data))
r = requests.post(url, data=json.dumps(form_data))
print(r.url)
print('-'*70)
print(r.text)





