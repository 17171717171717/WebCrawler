# ch7_2.py
from selenium import webdriver

driverPath = r'C:\Users\kaiwu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
print(type(browser))






