from pywhatkit import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def send_whats():
    phone = '+5511988110909'
    message = 'Bom dia pipis, dormiu bem?'
    pywhatkit.sendwhatmsg_instantly(phone, message,wait_time = 10 ,tab_close= True)
    print("Message sent")




get_wheather()