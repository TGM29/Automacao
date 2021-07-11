from pywhatkit import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def send_whats():
    phone = '+5511988110909'
    message = 'Bom dia pipis, dormiu bem?'
    pywhatkit.sendwhatmsg_instantly(phone, message,wait_time = 10 ,tab_close= True)
    print("Message sent")

def get_wheather():
    cidade = 'Campos do Jordão'
    #Declare the browser
    browser = webdriver.Chrome()
    #Open the site
    browser.get("https://www.climatempo.com.br")
    browser.find_element_by_xpath('//*[@id="bt_modalSearch_mobile"]/i').click()
    browser.find_element_by_xpath('//*[@id="searchGeneralMobile"]').click()
    browser.find_element_by_xpath('//*[@id="searchGeneralMobile"]').send_keys(cidade)
    temp_min = browser.find_element_by_xpath('//*[@id="current-weather-temperature"]').get_property('nodeValue')
    print(temp_min)


get_wheather()