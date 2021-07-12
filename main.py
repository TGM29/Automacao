from pywhatkit import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_wheather():
    #Declare the browser
    browser = webdriver.Chrome()
    #Open Climatempo
    browser.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/420/camposdojordao-sp')

    #Get what need
    temp_min = browser.find_element_by_xpath('//*[@id="min-temp-1"]').text
    temp_max = browser.find_element_by_xpath('//*[@id="max-temp-1"]').text
    chuva = browser.find_element_by_xpath('//*[@id="mainContent"]/div[5]/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[2]/div/span').text
    raios_uv = browser.find_element_by_xpath('//*[@id="mainContent"]/div[5]/div[4]/div[2]/div[2]/div[2]/ul/li[4]/div[2]/p[2]').text
    sol = browser.find_element_by_xpath('//*[@id="mainContent"]/div[5]/div[4]/div[2]/div[2]/div[2]/ul/li[6]/div[2]/p[2]').text

    phone = '+5511988110909'
    message = f'Bom dia,tudo bem?\nA temperatura máxima de hoje será de {temp_max} e mínima de {temp_min}.\nHoje a chance de chuva é de {chuva}.\nA incidencia de raios UV hoje é {raios_uv}, portanto {sol}.'

    pywhatkit.sendwhatmsg_instantly(phone, message, wait_time=10, tab_close=True)
    print("Message sent")


get_wheather()
