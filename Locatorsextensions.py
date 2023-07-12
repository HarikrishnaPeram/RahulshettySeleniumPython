#chrome driver invoking
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj= Service("C:/Users/selenium/work space/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https:rahulshettyacademy.com/client")
driver.find_element(By.CSS_SELECTOR, "body > app-root > app-login > div.banner > section:nth-child(2) > div > div.login-wrapper.my-auto.p-5 > a").click()