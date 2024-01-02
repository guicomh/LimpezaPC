import os
from tkinter import *
from tkinter import ttk

def limpar_temp():
    os.system("rd/s/q %temp%")
    os.system("cd.. && cd.. & cd.. && cd && cmd")

janela = Tk()

janela.title("Clean Magico")
janela.geometry("800x600")
fonte_personalizada = ("Arial", 20, "bold")

texto = Label(janela, text="CLEAN MAGICO 1.0", font=fonte_personalizada) . pack(pady=30)

botão_limpeza = Button(janela, text="Limpar", command=limpar_temp). pack(pady=20)

janela.mainloop()