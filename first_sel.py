from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https://www.google.com")
time.sleep(5)


'''
Output: 

Opens Browser and wait for 5 seconds
'''