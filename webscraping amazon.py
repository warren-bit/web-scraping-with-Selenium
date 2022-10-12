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
driver.get("https://www.amazon.com/b?node=283155")
search = driver.find_element("id", 'twotabsearchtextbox')
search.send_keys("books")
search.send_keys(Keys.RETURN)
data = []
try:
    books = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.ID, 'gridItemRoot'))
    )
    print(len(books))
    for book in books:
        title = book.find_element(By.TAG_NAME, 'span').text
        price = book.find_element(By.CLASS_NAME, '_cDEzb_p13n-sc-price_3mJ9Z').text
        data.append((title,price))
finally:
    driver.quit()