from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://www.globalsqa.com/demo-site/sliders/")
time.sleep(3)

frame = driver.find_element(By.CLASS_NAME, value="demo-frame")
driver.switch_to.frame(frame)

slider = driver.find_element(By.CSS_SELECTOR, value="#red > span")
actions = ActionChains(driver)

actions.click_and_hold(slider).move_by_offset(xoffset =  50, yoffset =  0).release().perform()
time.sleep(3)

print("SLIDER IS MOVING")
time.sleep(3)

driver.quit()

