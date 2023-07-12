from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:/Users/selenium/work space/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value")=="option2":
        checkbox.click()
        checkbox.is_selected()
        break
radiobuttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radiobuttons))

for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value")=="radio2":
        radiobutton.click()
        break
        #radiobutton.is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

