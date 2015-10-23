# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

driver = webdriver.Firefox()
driver.get("https://facebook.com/")

wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)

email_field = driver.find_element_by_id("email")
email_field.send_keys("user_email@email.com") # user_email

password_field = driver.find_element_by_id("pass")
password_field.send_keys("your_password") # your password
password_field.send_keys(Keys.RETURN)

print """Mission Completed!

    Find your new things in Facebook!
    
    See you later!
    "