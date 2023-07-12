from selenium import webdriver

from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")




service_obj= Service("C:/Users/selenium/work space/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
print(driver.title)





