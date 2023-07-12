#chrome driver invoking
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:/Users/selenium/work space/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https:rahulshettyacademy.com/angularpractice/")
#driver.find_element(By.NAME, "name").send_keys("Harikrishna")
driver.find_element(By.NAME, "email").send_keys("harikrishnaperam2@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Harikrishna2@")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()
successMessage = driver.find_element(By.CLASS_NAME, "alert-success").text

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Harikrishna")
print(successMessage)
assert "Success" in successMessage

