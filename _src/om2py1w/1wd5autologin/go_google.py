# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

reload(sys) # must reload
sys.setdefaultencoding('utf-8') # default encoding


print """ Explain:
    ==========
    
    * open a new Firefox browser
    * load the google homepage
    * search for "your_keywords"
    
    ==========
"""
your_keywords = sys.argv[1:]

browser = webdriver.Firefox()

browser.get("http://www.google.com")

search_elem = browser.find_element_by_name('q')

for keywords in your_keywords:
    search_elem.send_keys(keywords + " ")

search_elem.send_keys(Keys.RETURN)

print "Mission Completed!"