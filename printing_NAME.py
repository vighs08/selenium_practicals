from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://www.google.com")
elem = driver.find_element(By.CLASS_NAME, value = "gLFyf")
elem.click()
print(elem)
time.sleep(5)

'''
Output:

<selenium.webdriver.remote.webelement.WebElement (session="1fc0955a0bbb6fa2a5145113f8393977", element="f.DA84FFBFD2E7F41B74493EAD942D2C0A.d.E6D77F04F2A93CF56AFAAFA5131061EA.e.1")>
'''