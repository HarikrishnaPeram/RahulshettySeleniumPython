from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By



service_obj= Service("C:/Users/selenium/work space/chromedriver.exe")

Chrome_Options=webdriver.ChromeOptions()
Chrome_Options.add_argument("headless")
Chrome_Options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(service = service_obj, options=Chrome_Options)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR, "#tinymce").clear()
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("Iam started python automation")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)
#driver.get_screenshot_as_file("screenshot.jpg")

