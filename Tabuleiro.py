# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:45:35 2016

@author: Gabriel Noal
"""

import tkinter as tk
from EP import Jogo
Jogo = Jogo()
class Tabuleiro:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry("300x300")
        self.janela.rowconfigure(0, weight=2)
        self.janela.rowconfigure(1, weight=2)
        self.janela.rowconfigure(2, weight=2)
        self.janela.rowconfigure(3, weight=2)
        
        self.janela.columnconfigure(0, weight=2)
        self.janela.columnconfigure(1, weight=2)
        self.janela.columnconfigure(2, weight=2)
        
        self.caixa_de_texto = tk.Label(self.janela, text="Jogador X")
        self.caixa_de_texto.grid(row=3, column=0 , columnspan=3 )
        
        #if self.player == 1:
            
        
        self.botao_0_0 = tk.Button(self.janela)
        self.botao_0_0.configure(command= self.botao_0_0_clicado)
        self.botao_0_0.grid(row=0, column=0, stick="nsew")
        
        self.botao_0_1 = tk.Button(self.janela)
        self.botao_0_1.configure(command=Jogo.recebe_jogada(0,1))
        self.botao_0_1.grid(row=0, column=1, stick="nsew")

        self.botao_0_2 = tk.Button(self.janela)
        self.botao_0_2.configure(command=Jogo.recebe_jogada(0,2))
        self.botao_0_2.grid(row=0, column=2, stick="nsew")
        
        self.botao_1_0 = tk.Button(self.janela)
        self.botao_1_0.configure(command=Jogo.recebe_jogada(1,0))
        self.botao_1_0.grid(row=1, column=0, stick="nsew")

        self.botao_1_1 = tk.Button(self.janela)
        self.botao_1_1.configure(command=Jogo.recebe_jogada(1,1))
        self.botao_1_1.grid(row=1, column=1, stick="nsew")
        
        self.botao_1_2 = tk.Button(self.janela)
        self.botao_1_2.configure(command=Jogo.recebe_jogada(1,2))
        self.botao_1_2.grid(row=1, column=2, stick="nsew")
        
        self.botao_2_0 = tk.Button(self.janela)
        self.botao_2_0.configure(command=Jogo.recebe_jogada(2,0))
        self.botao_2_0.grid(row=2, column=0, stick="nsew")
        
        self.botao_2_1 = tk.Button(self.janela)
        self.botao_2_1.configure(command=Jogo.recebe_jogada(2,1))
        self.botao_2_1.grid(row=2, column=1, stick="nsew")

        self.botao_2_2 = tk.Button(self.janela)
        self.botao_2_2.configure(command=Jogo.recebe_jogada(2,2))
        self.botao_2_2.grid(row=2, column=2, stick="nsew")
                
        
    def botao_0_0_clicado(self):
        if Jogo.player == 1:
            self.botao_0_0.configure(text= "X")
            self.botao_0_0.configure(font = "Arial 10")
        else:
            self.botao_0_0.configure(text= "O")
            self.botao_0_0.configure(font = "Arial 10")
        Jogo.recebe_jogada(0,0)
        self.botao_0_0.configure(state="disable")
        
        
        
    def iniciar(self):
        self.janela.mainloop()
        
    
            
jogo_da_velha = Tabuleiro()
jogo_da_velha.iniciar()
