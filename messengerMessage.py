from msedge.selenium_tools import Edge, EdgeOptions
import selenium
import time
from selenium.webdriver.common.keys import Keys


message = input('Input message: ')
email = input('Input email: ')
password = input('Password: ')

options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)
driver.get('http://messenger.com')

loginButton = driver.find_element_by_id('loginbutton')
emailElem = driver.find_element_by_id('email')
passElem = driver.find_element_by_id('pass')
driver.implicitly_wait(10)
emailElem.send_keys(email)
passElem.send_keys(password)
loginButton.click()



person = driver.find_element_by_xpath("//span[text()='input_name_of_receiver']")
person.click()
time.sleep(3)
my_element = driver.find_element_by_css_selector(".notranslate._5rpu")
my_element.send_keys(message)
my_element.submit()




