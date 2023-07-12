

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
browsersortedveggies = []



service_obj= Service("C:/Users/selenium/work space/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#click on the column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
#collect all veggie names -> browser sorted
veggiewebelements = driver.find_elements(By.XPATH, " //tr/td[1]")
for ele in veggiewebelements:
    browsersortedveggies.append(ele.text)

originalBrowsersortedlist = browsersortedveggies .copy()
#browser sorted list = new sorted list
browsersortedveggies.sort()
# brwser sorted list = new sorted list
assert browsersortedveggies == originalBrowsersortedlist

