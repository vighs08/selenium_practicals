from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

dropdown = driver.find_element(By.XPATH,value="//select[@id='dropdown-class-example']")
select = Select(dropdown)
select.select_by_index(2)
time.sleep(2)
selected_option = select.first_selected_option.text

if selected_option == "Option2":
    print("Dropdown option selected successfully")
else:
    print("Dropdown option selection failed")
driver.quit()
