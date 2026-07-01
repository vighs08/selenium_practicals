from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.testfire.net/login.jsp")

username_field = driver.find_element(By.ID, "uid")
password_field = driver.find_element(By.ID, "passw")
submit_filed = driver.find_element(By.NAME, "btnSubmit")
username_field.send_keys("admin")
password_field.send_keys("admin")
submit_filed.click()

time.sleep(2)
driver.back()

time.sleep(2)
driver.forward()

time.sleep(2)
driver.refresh()

time.sleep(2)

print(f"Title: {driver.title}")
print(f"Url: {driver.current_url}")

driver.quit()

