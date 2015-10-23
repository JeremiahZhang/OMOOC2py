# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

driver = webdriver.Firefox()
driver.get('https://mp.weixin.qq.com/')

wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)

wechat_account = driver.find_element_by_id("account")
wechat_account.send_keys("user@email.com")      # input your email address or your wechat account

your_password = driver.find_element_by_id("pwd")
your_password.send_keys("balabalabala")         # your password instead of balabalabala
your_password.send_keys(Keys.RETURN)

print "Mission Completed! Write your new article.-->"