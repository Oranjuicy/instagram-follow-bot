from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException
import time

INSTAGRAM_USWERNAME = "ryke.ceramics"
URL = "https://www.instagram.com/pottery_west/?hl=en"
PASSWORD = "LG74nUhe28BE25x"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)

driver.get(URL)
time.sleep(3)
login = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/div/div/div[3]/div[1]/a")
login.click()
time.sleep(3)
username = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")
username.send_keys(INSTAGRAM_USWERNAME)
password = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

