from lib2to3.pgen2 import driver
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

s = Service(r"./driver/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.linkedin.com/home")
# loging in
email_box = driver.find_element(By.XPATH, '//*[@id="session_key"]')
email_box.send_keys("shanefilan055@gmail.com")
password_box = driver.find_element(By.XPATH, '//*[@id="session_password"]')
password_box.send_keys("K^&P/jKs^A=#5tJ")
sign_in = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button')
sign_in.click()
time.sleep(5)

# searching for jobs
search_box = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
search_box.send_keys("cyber security jobs")
search_box.send_keys(Keys.RETURN)
time.sleep(5)
# see all jobs
all_jobs = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/div[2]/a')
all_jobs.click()
time.sleep(5)

chart = driver.find_element(By.CLASS_NAME, 'scaffold-layout__list-container')
jobs = chart.find_element(By.TAG_NAME, 'li')
print(len(jobs))
