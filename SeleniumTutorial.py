from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

# deprecated:
# driver = webdriver.Chrome(PATH)
driver = webdriver.Chrome(service=Service(PATH))
driver.get('https://www.google.com/')
assert 'Google' in (driver.title), driver.quit()

# We'll have to accept google conditions first
# fin_element_by methods are deprecated as well
#button = driver.find_element_by_id('L2AGLb')
button = driver.find_element(By.ID,'L2AGLb')
button.send_keys(Keys.RETURN)

# Using HTML to access objects
# More common ways to access:
# 1. Id
# 2. Name 
# 3. ClassName
# Class is not recommended as it is not gonna be unic like Id

search = driver.find_element(By.NAME,'q')
search.send_keys('Sofía Andújar Muñoz')
search.send_keys(Keys.RETURN) # RETURN is ENTER


driver.quit()