# -*- coding: utf-8 _*-
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

driver = webdriver.Firefox()
driver.get('http://www.iomooc.com/')

wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)

github_login_button = driver.find_element_by_link_text("GitHub")
github_login_button.send_keys(Keys.RETURN)

# in github sign in
email_field = driver.find_element_by_id("login_field")
email_field.send_keys("zhangleisuda@gmail.com") # user_email

password_field = driver.find_element_by_id("password")
password_field.send_keys("focusonstudy@4") # your password
password_field.send_keys(Keys.RETURN)

print "Mission Completed! Write your new article.-->"