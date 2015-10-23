# -*- coding: utf-8 _*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print """ Example 1:
    ==========
    
    * open a new Firefox browser
    * load the google homepage
    * search for "github"
    * close the browser
    
"""

browser = webdriver.Firefox()             # open your firefox browser

browser.get("http://www.google.com")      # go to google webpage
assert 'Google' in browser.title          # confirm that title has “Google” word in it

# browser.get("http://www.google.com")
# assert 'google' in browser.title

elem = browser.find_element_by_name('q')  # name = "q" is in the search field of the google webpage source code 
elem.send_keys('github' + Keys.RETURN)    # search keyword Keys.RETURN like keyboard enter or Go
print "Mission Completed!"

# browser.quit()