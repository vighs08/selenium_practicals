from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://github.com")
print("Current Url: ", driver.current_url)
print("Title: ", driver.title)
time.sleep(5)
driver.quit()

# '''
# '''
