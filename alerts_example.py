from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("file:///home/girish/Downloads/alerts_example.html")
time.sleep(3)
driver.find_element(By.XPATH, value="//button[@onclick='jsAlert()']").click()
time.sleep(3)
alert = driver.switch_to.alert
print(f"Alert text is : {alert.text}")
alert.accept()

time.sleep(3)
driver.quit()
