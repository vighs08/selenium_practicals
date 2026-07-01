from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/nested_frames")

top = driver.find_element(By.NAME, value="frame-top")
driver.switch_to.frame("frame-top")

left = driver.find_element(By.NAME, value="frame-left")
driver.switch_to.frame("frame-left")

driver.switch_to.default_content()
driver.switch_to.frame("frame-top")

middle = driver.find_element(By.NAME, value="frame-middle")
driver.switch_to.frame("frame-middle")

driver.switch_to.default_content()
driver.switch_to.frame("frame-top")

right = driver.find_element(By.NAME, value="frame-right")
driver.switch_to.frame("frame-right")

driver.switch_to.default_content()

bottom = driver.find_element(By.NAME, value="frame-bottom")
driver.switch_to.frame("frame-bottom")

driver.switch_to.default_content()
time.sleep(3)
driver.quit()
