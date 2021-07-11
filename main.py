from pywhatkit import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def send_whats():
    phone = '+5511988110909'
    message = 'Bom dia pipis, dormiu bem?'
    pywhatkit.sendwhatmsg_instantly(phone, message,wait_time = 10 ,tab_close= True)
    print("Message sent")

def get_wheather():
    #Declare the browser
    browser = webdriver.Chrome()
    #Open Climatempo
    browser.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/420/camposdojordao-sp')
    temp_min = browser.find_element_by_xpath('/html/body/div[4]/div[5]/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[1]/div/p/span[1]').text
    print(temp_min)



    #Open the site
    dolar = browser.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')



get_wheather()