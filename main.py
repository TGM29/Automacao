from pywhatkit import *

def send_whats():
    phone = '+5511988110909'
    message = 'Bom dia pipis, dormiu bem?'
    pywhatkit.sendwhatmsg_instantly(phone, message, 2, False)
    print("Message sent")

send_whats()