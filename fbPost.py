import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/?stype=lo&jlou=AfepT-WrekrwrbThp14svDOVKZJ-VxvUMRqkcUdagoA4Uf9a88BdqjjPO7kT_JtEmPWYajYI4LOhlwGzKg4VbwuK0kubCEm4smUhKHJsVdf86g&smuh=57832&lh=Ac9J_2GzcYO7NajY")
inputElement = driver.find_element_by_id("email")
inputElement.send_keys('riteshm594@gmail.com')
password = driver.find_element_by_id("pass")
password.send_keys('unowhoim')
inputElement.submit()
#keyword = driver.find_element_by_class_name('_1mf _1mj')
#keyword.send_keys('Anonymous POST')
#keyword.submit()
#link.click()
#link = driver.find_element_by_css_selector("a-button-text")
#link.click()
#driver.quit()
