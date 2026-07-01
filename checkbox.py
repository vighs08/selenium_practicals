from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("https://demoqa.com/checkbox")

elem = driver.find_element(By.XPATH,value="//span[@aria-label='Select Home']")
time.sleep(5)
elem.click()
time.sleep(5)

if not elem.is_selected():
    print("Checkbox selected successfully")
else:
    print("Checkbox selection failed")

time.sleep(5)
elem.click()
time.sleep(5)

driver.quit()
