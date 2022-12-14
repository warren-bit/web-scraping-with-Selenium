from lib2to3.pgen2 import driver
from turtle import title
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# get url
s = Service(r"./driver/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.linkedin.com/home")

# signing in to linkedin
class sign_in:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def log_in(self):
        email_box = driver.find_element(By.XPATH, '//*[@id="session_key"]')
        email_box.send_keys(self.email)
        password_box = driver.find_element(By.XPATH, '//*[@id="session_password"]')
        password_box.send_keys(self.password)
        sign_in_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button')
        sign_in_button.click()
        time.sleep(5)

# categorizing the jobs
class jobs:
    def __init__(self, job_category):
        self.job_category = job_category
    
    def search_jobs(self):
        search_box = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
        search_box.send_keys(self.job_category)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)
        # see all jobs
        all_jobs = driver.find_element(By.CLASS_NAME, 'app-aware-link ')
        all_jobs.click()
        time.sleep(5)

    def find_jobs(self):
        t = driver.find_element(By.TAG_NAME, 'ul')
        job = t.find_elements(By. TAG_NAME, 'li')
        print("Number of jobs:", len(job))

sign = sign_in("shanefilan055@gmail.com", "K^&P/jKs^A=#5tJ")
sign.log_in()
job = jobs("cyber security jobs")
job.search_jobs()
job.find_jobs()
driver.quit()