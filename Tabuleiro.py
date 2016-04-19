# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:45:35 2016

@author: Gabriel Noal
"""

import tkinter as tk
class Tabuleiro:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry("300x300")
        self.janela.rowconfigure(0, weight=2)
        self.janela.rowconfigure(1, weight=2)
        self.janela.rowconfigure(2, weight=2)
        self.janela.rowconfigure(3, weight=1)
        
        self.janela.columnconfigure(0, weight=1)
        self.janela.columnconfigure(1, weight=1)
        self.janela.columnconfigure(2, weight=1)
        
        self.caixa_de_texto = tk.Label(3, text="")
        
        self.botao_0_0 = tk.Button(self.janela)
        #self.botao_0_0.configure(command=)
        self.botao_0_0.grid(row=0, column=0, stick="nsew")
        
        self.botao_0_1 = tk.Button(self.janela)
        #self.botao_0_1.configure(command=#futuro comando)
        self.botao_0_1.grid(row=0, column=1, stick="nsew")

        self.botao_0_2 = tk.Button(self.janela)
        #self.botao_0_2.configure(command=#futuro comando)
        self.botao_0_2.grid(row=0, column=2, stick="nsew")
        
        self.botao_1_0 = tk.Button(self.janela)
        #self.botao_1_0.configure(command=#futuro comando)
        self.botao_1_0.grid(row=1, column=0, stick="nsew")

        self.botao_1_1 = tk.Button(self.janela)
        #self.botao_1_1.configure(command=#futuro comando)
        self.botao_1_1.grid(row=1, column=1, stick="nsew")
        
        self.botao_1_2 = tk.Button(self.janela)
        #self.botao_1_2.configure(command=#futuro comando)
        self.botao_1_2.grid(row=1, column=2, stick="nsew")
        
        self.botao_2_0 = tk.Button(self.janela)
        #self.botao_2_0.configure(command=#futuro comando)
        self.botao_2_0.grid(row=2, column=0, stick="nsew")
        
        self.botao_2_1 = tk.Button(self.janela)
        #self.botao_2_1.configure(command=#futuro comando)
        self.botao_2_1.grid(row=2, column=1, stick="nsew")

        self.botao_2_2 = tk.Button(self.janela)
        #self.botao_2_2.configure(command=#futuro comando)
        self.botao_2_2.grid(row=2, column=2, stick="nsew")
        
        
    def iniciar(self):
        self.janela.mainloop()
            
jogin = Tabuleiro()
jogin.iniciar()
