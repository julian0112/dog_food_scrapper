# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.by import By
# import time
# import random

# service = Service(executable_path="geckodriver.exe")

# options = webdriver.FirefoxOptions()
# options.headless = True

# driver = webdriver.Firefox(options=options, service=service)

# driver.get("https://www.todomascotascr.com/277-alimento-y-galletas-para-perro")

# counter = 0

# food_options = driver.find_elements(By.XPATH, '//div[@class="thumbnail-container clearfix reviews-loading"]')

# for food in food_options:
#     title = food.find_element(By.XPATH, '//div[@class="product-info"]').text
    
#     print(title)

from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.todomascotascr.com/277-alimento-y-galletas-para-perro').text

soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all('div', class_ = 'thumbnail-container clearfix reviews-loading').div

for product in products:
    
    
    
    
    title = product.find('h1', class_ = 'h3 product-title').text
    print(title)