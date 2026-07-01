from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
# driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")
print(f"Page title: {driver.title}")
print(f"Current URL: {driver.current_url}")

assert "Internet" in driver.title
assert "the-internet" in driver.current_url

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.XPATH, '//*[@id="login"]/button')

time.sleep(2)

assert "secure" in driver.current_url
ele = driver.find_element(By.ID, "flash")
assert "You logged into a secure area!" in ele.text

time.sleep(5)
driver.quit()
print("Successfully did operation")

