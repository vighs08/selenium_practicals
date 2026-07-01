from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://www.google.com")
elem = driver.find_element(By.CSS_SELECTOR, value='#APjFqb')
elem.click()
print(elem)
elem = driver.find_element(By.TAG_NAME, value='textarea')
elem.click()
print(elem)
elem = driver.find_element(By.XPATH, value='//*[@id="APjFqb"]')
elem.click()
print(elem)
time.sleep(5)

'''
Output:

<selenium.webdriver.remote.webelement.WebElement (session="9762c13e567ced1750cbc39e9fbfda7b", element="f.211906C103D8EC2F7D9086E1AD13B93F.d.E7F671DC32FBAF4DDE9AAF0FED108ED6.e.2")>
<selenium.webdriver.remote.webelement.WebElement (session="9762c13e567ced1750cbc39e9fbfda7b", element="f.211906C103D8EC2F7D9086E1AD13B93F.d.E7F671DC32FBAF4DDE9AAF0FED108ED6.e.2")>
<selenium.webdriver.remote.webelement.WebElement (session="9762c13e567ced1750cbc39e9fbfda7b", element="f.211906C103D8EC2F7D9086E1AD13B93F.d.E7F671DC32FBAF4DDE9AAF0FED108ED6.e.2")>
'''