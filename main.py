from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chromedriver_path = "chromedriver/chromedriver.exe"
chrome_options = Options()

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.google.com")


search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("lequangkhai.id.vn")
search_box.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()
