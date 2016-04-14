
		#command_executor="http://192.168.43.149:4444/wd/hub",

#file test_1.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Remote(
   command_executor='http://192.168.43.149:4444/wd/hub',
   desired_capabilities={
            #"browserName": "internet explorer"})
            #"browserName": "chrome"})
            "browserName": "firefox"})

driver.implicitly_wait(30)
driver.maximize_window() # If platform is Linux instead use: driver.set_window_size(1920,1080)


def test_one():
	try:
		driver.get("http://python.org/")
		#assert "Python" in driver.title
		elem = driver.find_element_by_name("q")
		elem.send_keys("documentation")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source
	finally:
		print ("Test One - Video: " + driver.session_id)
		driver.quit()
test_one()
