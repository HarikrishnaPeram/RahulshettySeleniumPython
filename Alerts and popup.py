from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By

service_obj= Service("C:/Users/selenium/work space/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Harikrishna")
driver.find_element(By.ID, "alertbtn").click()
alert=driver.switch_to.alert
alertText= alert.text
print(alertText)
alert.accept()
