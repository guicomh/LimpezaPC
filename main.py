import os
from tkinter import *


def limpar_temp():
    os.system("rd/s/q %temp%")
    os.system("cd .. && cd .. & cd.. && cd.. && cd .. && cd .. && cd .. && cd Windows && rd/s/q temp")

janela = Tk()

janela.iconbitmap("icone.ico")
janela.title("Clean Magico")
janela.geometry("800x600")
fonte_personalizada = ("Arial", 20, "bold")



texto = Label(janela, text="CLEAN MAGICO 1.0", font=fonte_personalizada) . pack(pady=30)

botão_limpeza = Button(janela, text="Limpar", command=limpar_temp, font=("Arial", 12, "bold")) . pack(pady=20)



janela.mainloop()