from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

elem = driver.find_element(By.XPATH,value="//input[@value='radio3']")
time.sleep(1)
elem.click()
time.sleep(1)

elem = driver.find_element(By.XPATH,value="//input[@value='radio2']")
time.sleep(1)
elem.click()
time.sleep(1)

elem = driver.find_element(By.XPATH,value="//input[@value='radio1']")
time.sleep(1)
elem.click()
time.sleep(1)

if elem.is_selected():
    print("Radio box selected")
else:
    print("Radio box selection failed")

print("Test Successfull done")
driver.quit()
