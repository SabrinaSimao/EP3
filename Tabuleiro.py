# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:45:35 2016

@author: Usuario
"""

import tkinter as tk
class Tabuleiro:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry("300x350")
        self.janela.rowconfigure(0,"100", wight=1)
        self.janela.rowconfigure(1,"100", wight=1)
        self.janela.rowconfigure(2,"100", wight=1)
        
        self.janela.columnconfigure(0,"100", wight=1)
        self.janela.columnconfigure(1,"100", wight=1)
        self.janela.columnconfigure(2,"100", wight=1)
        
        self.botao_0_0= tk.Button(self.janela)
        self.botao_0_0.configure(comand=#futuro comando)
        self.botao_0_0.grid(row=0, colum=1, sick="nsew")
        
        self.botao_0_1= tk.Button(self.janela)

        self.botao_0_2= tk.Button(self.janela)

        self.botao_1_0= tk.Button(self.janela)

        self.botao_1_1= tk.Button(self.janela)

        self.botao_1_2= tk.Button(self.janela)

        self.botao_2_0= tk.Button(self.janela)

        self.botao_2_1= tk.Button(self.janela)

        self.botao_2_2= tk.Button(self.janela)
