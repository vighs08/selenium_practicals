from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(5.1)
driver.get("https://www.hyrtutorials.com/p/waits-demo.html")

textbox1 = driver.find_element(By.XPATH, value="//button[@id='btn1']")
textbox2 = driver.find_element(By.XPATH, value="//button[@id='btn2']")

textbox1.click()
textbox2.click()

tb1 = driver.find_element(By.ID, "txt1")
print("Placeholder for TB1 is:", tb1.get_attribute("placeholder"))
tb2 = driver.find_element(By.ID, "txt2")

# Print the placeholder attribute
print("Placeholder for TB2 is:", tb2.get_attribute("placeholder"))

print("Textboxes appeared and placeholders were retrieved!")
driver.quit()
