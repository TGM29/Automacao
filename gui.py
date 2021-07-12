from tkinter import *

def pega_tel():
    telefone = entrada.get()
    print(telefone)

#Declara a Tela
tela = Tk()
#Titulo para a Tela
tela.title("Tempo + Whats")
#Cria a entrada do telefone
entrada = Entry(tela,text = 'Telefone', width=35, borderwidth=5)
entrada.pack()
#Cria o botão para enviar
button_1 = Button(tela,text="Mandar Mensagem", padx=40, pady=20, command = pega_tel)
button_1.pack()








tela.mainloop()