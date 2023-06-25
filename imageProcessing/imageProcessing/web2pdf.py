from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://80.2.242.14:81/index2test.html')
sleep(1)

driver.get_screenshot_as_file("screenshot.png")
driver.quit()

print("end")