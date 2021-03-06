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

email_field = driver.find_element_by_id("email")
email_field.send_keys("youremail@email.com") # user_email

password_field = driver.find_element_by_id("password")
password_field.send_keys("yourpassword") # your password

login_field = driver.find_element_by_id("login")
login_field.send_keys(Keys.RETURN)

print "Mission Completed! Go Openmind and then Renew Mind!--->"