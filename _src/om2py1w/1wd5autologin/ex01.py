# -*- coding: utf-8 _*-
from selenium import webdriver


print """ # function:

    1- open a new Firefox browser
    2- load the webpage at the given URL

    HAVE FUN

"""

browser = webdriver.Firefox()
browser.get("http://seleniumhq.org/")