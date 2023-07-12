from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait


service_obj= Service("C:/Users/selenium/work space/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/angularpractice/shop")
#click on shop
driver.find_element(By.XPATH, "//a[.='Shop']").click()
#Grab all the products
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products :
    productName =  product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry:":

        product.find_element(By.XPATH, "div/button").click()
print(productName)
#goto check out page
driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
#check out from that page
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
#select country from auto suggestive drop down
driver.find_element(By.ID, "country").send_keys("Ind")
wait = WebDriverWait (driver,10)
wait.until(expected_conditions.presence_of_element_located((By.ID, "country")))
#select country and chick on the purchase
driver.find_element(By.XPATH, "//a[.='India']").click()
driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
#verify the succes message
SuccesText = driver.find_element(By.CSS_SELECTOR, "div[class*='alert alert-success alert-dismissible']").text

assert "Success! Thank you!" in SuccesText

print(SuccesText)
