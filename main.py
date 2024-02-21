import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def limpar_temp():
    os.system("rd/s/q %temp%") 

janela = Tk()

janela.resizable(False, False)

imagem_fundo = Image.open("fundo.png")
janela.iconbitmap("icone.ico")
janela.title("Limpeza Pc")
janela.geometry("800x600")
fonte_personalizada = ("Arial", 20, "bold")
fonte_texto = ("Arial", 14)



botão_limpeza = Button(janela, text=" Limpeza ", command=limpar_temp, font=("Arial", 12, "bold")) . pack()


janela.mainloop()
