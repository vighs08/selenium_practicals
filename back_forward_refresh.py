
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in")

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("books")
search.send_keys(Keys.RETURN)

time.sleep(2)
driver.back()

time.sleep(2)
driver.forward()

driver.refresh()

print(f"Title: {driver.title}")
print(f"Url: {driver.current_url}")

driver.quit()
