from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

s = Service(r"./driver/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.youtube.com/")
search = driver.find_element(By.XPATH,'//*[@id="search-input"]')
search.send_keys("arsenal")
search.send_keys(Keys.RETURN)
# driver.quit()