from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("C:\drivers\chromedriver")
driver.get("http://www.python.org")
assert "Python" in driver.title
time.sleep(5)
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(5)
driver.close()