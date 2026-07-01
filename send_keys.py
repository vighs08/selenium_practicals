from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/login")

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")
submit_button.click()

time.sleep(5)
driver.quit()
