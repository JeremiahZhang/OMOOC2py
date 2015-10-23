# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print """ Example 1:
    ==========
    
    * open a new Firefox browser
    * load the google homepage
    * search for "your_keywords"
    
"""
your_keywords = sys.argv[1:]

browser = webdriver.Firefox()             # open your firefox browser

browser.get("http://www.google.com")      # go to google webpage
assert 'Google' in browser.title          # confirm that title has “Google” word in it

elem = browser.find_element_by_name('q')  # name = "q" is in the search field of the google webpage source code

for keywords in your_keywords:
    elem.send_keys(keywords + " ")

elem.send_keys(Keys.RETURN)    # search keyword Keys.RETURN like keyboard enter or Go

print "Mission Completed!"