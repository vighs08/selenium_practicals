from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/iframe")
elem = driver.find_element(By.ID, value="mce_0_ifr")
driver.switch_to.frame("mce_0_ifr")
textarea = driver.find_element(By.ID, "tinymce")
driver.switch_to.default_content()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#page-footer > div > div > a").click()
time.sleep(2)
driver.quit()
