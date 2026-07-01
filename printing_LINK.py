from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.get("http://www.google.com")
elem = driver.find_element(By.XPATH, value="//a[contains(@aria-label,'Gmail')]")
elem.click()
print(elem)
elem = driver.find_element(By.TAG_NAME, value='a')
elem.click()
print(elem)
# elem = driver.find_element(By.XPATH, value='/html/body/div[2]/div[2]/div/div')
# elem.click()
# print(elem)
elem = driver.find_element(By.LINK_TEXT, value='Gmail')
elem.click()
print(elem)
time.sleep(5)
