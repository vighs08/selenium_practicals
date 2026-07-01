from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://www.google.com")
elem = driver.find_element(By.ID, value="APjFqb")
elem.click()
print(elem)
time.sleep(5)

'''
Output:

<selenium.webdriver.remote.webelement.WebElement (session="21405e93b55f10433070cc5cdb6b77df", element="f.BB8E83607DBDA00750269CDA3C94450B.d.A007122B690F62FB618636D85DAF42F0.e.1")>
'''