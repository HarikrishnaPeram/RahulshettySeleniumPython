from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By



service_obj= Service("C:/Users/selenium/work space/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

widowsOpen=driver.window_handles
driver.switch_to.window(widowsOpen[1])
#driver.switch_to.window(widowsOpen[0])
print(driver.find_element(By.TAG_NAME, "h3").text)