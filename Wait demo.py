import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("C:/Users/selenium/work space/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

expectedlist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actuallist = []
#implicit wait

driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

time.sleep(1)

wait = WebDriverWait (driver, 5)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='products']/div/div/button")))

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = (len(results))
assert count > 0
print(count)
for result in results:
    actuallist.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()
assert  expectedlist == actuallist

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > div > div > button").click()
#time.sleep(10)

#eplicit wait
wait = WebDriverWait (driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#root > div > div > div > div > div > span")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

#sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum+int(price.text)
print(sum)
totalamount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == int(totalamount)

totaldiscount=float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert totalamount >totaldiscount


