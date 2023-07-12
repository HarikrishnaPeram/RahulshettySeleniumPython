#chrome driver invoking
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj= Service("C:/Users/selenium/work space/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https:rahulshettyacademy.com")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
driver.get("https:rahulshettyacademy.com/seleniumPractise/#/")
print(driver.current_url)
print(driver.title)
driver.minimize_window()
driver.back()
print(driver.current_url)
print(driver.title)
driver.close()





