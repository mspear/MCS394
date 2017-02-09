__author__ = 'mspear'
from selenium import webdriver

import time


driver = webdriver.Chrome('/Users/mspear/Downloads/chromedriver')
driver.get('http://www.wikipedia.org')
time.sleep(5)

link = driver.find_element_by_partial_link_text('English')
link.click()

time.sleep(5)

search_box = driver.find_element_by_id('searchInput')
search_box.send_keys('Hello Kitty')
search_box.submit()
time.sleep(5)
print(driver.page_source)
driver.quit()


//micahel my penis