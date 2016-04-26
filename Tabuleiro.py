# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:45:35 2016

@author: Gabriel Noal
"""

import tkinter as tk
from EP import Jogo
jogo = Jogo()
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
        
        self.caixa_de_texto = tk.Label(self.janela, text= "Vez do X")
        self.caixa_de_texto.configure(font= "Courie 10")        
        self.caixa_de_texto.grid(row=3, column=0 , columnspan=2 )

            
        
        self.botao_0_0 = tk.Button(self.janela)
        self.botao_0_0.configure(command= self.botao_0_0_clicado)
        self.botao_0_0.grid(row=0, column=0, stick="nsew")
        
        self.botao_0_1 = tk.Button(self.janela)
        self.botao_0_1.configure(command= self.botao_0_1_clicado)
        self.botao_0_1.grid(row=0, column=1, stick="nsew")

        self.botao_0_2 = tk.Button(self.janela)
        self.botao_0_2.configure(command= self.botao_0_2_clicado)
        self.botao_0_2.grid(row=0, column=2, stick="nsew")
        
        self.botao_1_0 = tk.Button(self.janela)
        self.botao_1_0.configure(command= self.botao_1_0_clicado)
        self.botao_1_0.grid(row=1, column=0, stick="nsew")

        self.botao_1_1 = tk.Button(self.janela)
        self.botao_1_1.configure(command= self.botao_1_1_clicado)
        self.botao_1_1.grid(row=1, column=1, stick="nsew")
        
        self.botao_1_2 = tk.Button(self.janela)
        self.botao_1_2.configure(command= self.botao_1_2_clicado)
        self.botao_1_2.grid(row=1, column=2, stick="nsew")
        
        self.botao_2_0 = tk.Button(self.janela)
        self.botao_2_0.configure(command= self.botao_2_0_clicado)
        self.botao_2_0.grid(row=2, column=0, stick="nsew")
        
        self.botao_2_1 = tk.Button(self.janela)
        self.botao_2_1.configure(command= self.botao_2_1_clicado)
        self.botao_2_1.grid(row=2, column=1, stick="nsew")

        self.botao_2_2 = tk.Button(self.janela)
        self.botao_2_2.configure(command= self.botao_2_2_clicado)
        self.botao_2_2.grid(row=2, column=2, stick="nsew")
        
        self.botao_reiniciar= tk.Button(self.janela)        
        self.botao_reiniciar.configure(text= "Reiniciar")
        self.botao_reiniciar.configure(font= "Courier 10")
        self.botao_reiniciar.configure(command=self.reiniciar)
        self.botao_reiniciar.grid(row=3, column=2, columnspan=3, stick="nsew")
        
        #self.reiniciar

        
    def botao_0_0_clicado(self):
        if jogo.player == 1:
            self.botao_0_0.configure(text= "X")
            self.botao_0_0.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do O")
            self.caixa_de_texto.configure(font= "Courie 10")
        else:
            self.botao_0_0.configure(text= "O")
            self.botao_0_0.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do X")
            self.caixa_de_texto.configure(font= "Courie 10")
        jogo.recebe_jogada(0,0)
        self.botao_0_0.configure(state="disable")
        
        if jogo.verifica_ganhador() == 1:
            self.caixa_de_texto.configure(text= "X GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
        elif jogo.verifica_ganhador()==2:
            self.caixa_de_texto.configure(text= "O GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
            print("O Ganhou")
        elif jogo.verifica_ganhador() == 0:
            self.caixa_de_texto.configure(text= "DEU VELHA")
            self.caixa_de_texto.configure(font= "Courie 10")            
            print("deu velha")
            self.reiniciar
        
    def botao_0_1_clicado(self):
        if jogo.player == 1:
            self.botao_0_1.configure(text= "X")
            self.botao_0_1.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do O")
            self.caixa_de_texto.configure(font= "Courie 10")
        else:
            self.botao_0_1.configure(text= "O")
            self.botao_0_1.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do X")
            self.caixa_de_texto.configure(font= "Courie 10")
        jogo.recebe_jogada(0,1)
        self.botao_0_1.configure(state="disable")

        if jogo.verifica_ganhador() == 1:
            self.caixa_de_texto.configure(text= "X GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
        elif jogo.verifica_ganhador()==2:
            self.caixa_de_texto.configure(text= "O GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
            print("O Ganhou")
        elif jogo.verifica_ganhador() == 0:
            self.caixa_de_texto.configure(text= "DEU VELHA")
            self.caixa_de_texto.configure(font= "Courie 10")
            print("deu velha")
            self.reiniciar
        else:
            pass
        
    def botao_0_2_clicado(self):
        if jogo.player == 1:
            self.botao_0_2.configure(text= "X")
            self.botao_0_2.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do O")
            self.caixa_de_texto.configure(font= "Courie 10")
        else:
            self.botao_0_2.configure(text= "O")
            self.botao_0_2.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do X")
            self.caixa_de_texto.configure(font= "Courie 10")
        jogo.recebe_jogada(0,2)
        self.botao_0_2.configure(state="disable")

        if jogo.verifica_ganhador() == 1:
            self.caixa_de_texto.configure(text= "X GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
        elif jogo.verifica_ganhador()==2:
            self.caixa_de_texto.configure(text= "O GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
            print("O Ganhou")
        elif jogo.verifica_ganhador() == 0:
            self.caixa_de_texto.configure(text= "DEU VELHA")
            self.caixa_de_texto.configure(font= "Courie 10")
            print("deu velha")
            self.reiniciar
        else:
            pass
        
    def botao_1_0_clicado(self):
        if jogo.player == 1:
            self.botao_1_0.configure(text= "X")
            self.botao_1_0.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do O")
            self.caixa_de_texto.configure(font= "Courie 10")
        else:
            self.botao_1_0.configure(text= "O")
            self.botao_1_0.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do X")
        jogo.recebe_jogada(1,0)
        self.botao_1_0.configure(state="disable")

        if jogo.verifica_ganhador() == 1:
            self.caixa_de_texto.configure(text= "X GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
        elif jogo.verifica_ganhador()==2:
            self.caixa_de_texto.configure(text= "O GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
            print("O Ganhou")
        elif jogo.verifica_ganhador() == 0:
            self.caixa_de_texto.configure(text= "DEU VELHA")
            self.caixa_de_texto.configure(font= "Courie 10")
            print("deu velha")
            self.reiniciar
        else:
            pass    

    def botao_1_1_clicado(self):
        if jogo.player == 1:
            self.botao_1_1.configure(text= "X")
            self.botao_1_1.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do O")
            self.caixa_de_texto.configure(font= "Courie 10")
        else:
            self.botao_1_1.configure(text= "O")
            self.botao_1_1.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do X")
            self.caixa_de_texto.configure(font= "Courie 10")
        jogo.recebe_jogada(1,1)
        self.botao_1_1.configure(state="disable")

        if jogo.verifica_ganhador() == 1:
            self.caixa_de_texto.configure(text= "X GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
        elif jogo.verifica_ganhador()==2:
            self.caixa_de_texto.configure(text= "O GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
            print("O Ganhou")
        elif jogo.verifica_ganhador() == 0:
            self.caixa_de_texto.configure(text= "DEU VELHA")
            self.caixa_de_texto.configure(font= "Courie 10")
            print("deu velha")
            self.reiniciar
        else:
            pass
        
    def botao_1_2_clicado(self):
        if jogo.player == 1:
            self.botao_1_2.configure(text= "X")
            self.botao_1_2.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do O")
            self.caixa_de_texto.configure(font= "Courie 10")
        else:
            self.botao_1_2.configure(text= "O")
            self.botao_1_2.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do X")
            self.caixa_de_texto.configure(font= "Courie 10")
        jogo.recebe_jogada(2,0)
        self.botao_1_2.configure(state="disable")

        if jogo.verifica_ganhador() == 1:
            self.caixa_de_texto.configure(text= "X GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
        elif jogo.verifica_ganhador()==2:
            self.caixa_de_texto.configure(text= "O GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
            print("O Ganhou")
        elif jogo.verifica_ganhador() == 0:
            self.caixa_de_texto.configure(text= "DEU VELHA")
            self.caixa_de_texto.configure(font= "Courie 10")
            print("deu velha")
            self.reiniciar

        
    def botao_2_0_clicado(self):
        if jogo.player == 1:
            self.botao_2_0.configure(text= "X")
            self.botao_2_0.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do O")
            self.caixa_de_texto.configure(font= "Courie 10")
        else:
            self.botao_2_0.configure(text= "O")
            self.botao_2_0.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do X")
            self.caixa_de_texto.configure(font= "Courie 10")
        jogo.recebe_jogada(2,0)
        self.botao_2_0.configure(state="disable")

        if jogo.verifica_ganhador() == 1:
            self.caixa_de_texto.configure(text= "X GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
        elif jogo.verifica_ganhador()==2:
            self.caixa_de_texto.configure(text= "O GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
            print("O Ganhou")
        elif jogo.verifica_ganhador() == 0:
            self.caixa_de_texto.configure(text= "DEU VELHA")
            self.caixa_de_texto.configure(font= "Courie 10")
            print("deu velha")
            self.reiniciar
        else:
            pass    

    def botao_2_1_clicado(self):
        if jogo.player == 1:
            self.botao_2_1.configure(text= "X")
            self.botao_2_1.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do O")
            self.caixa_de_texto.configure(font= "Courie 10")
        else:
            self.botao_2_1.configure(text= "O")
            self.botao_2_1.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do X")
            self.caixa_de_texto.configure(font= "Courie 10")
        jogo.recebe_jogada(2,1)
        self.botao_2_1.configure(state="disable")

        if jogo.verifica_ganhador() == 1:
            self.caixa_de_texto.configure(text= "X GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
        elif jogo.verifica_ganhador()==2:
            self.caixa_de_texto.configure(text= "O GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
            print("X Ganhou")
        elif jogo.verifica_ganhador() == 0:
            self.caixa_de_texto.configure(text= "DEU VELHA")
            self.caixa_de_texto.configure(font= "Courie 10")
            print("deu velha")
            self.reiniciar
        
    def botao_2_2_clicado(self):
        if jogo.player == 1:
            self.botao_2_2.configure(text= "X")
            self.botao_2_2.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do O")
            self.caixa_de_texto.configure(font= "Courie 10")
        else:
            self.botao_2_2.configure(text= "O")
            self.botao_2_2.configure(font = "Courie 10")
            self.caixa_de_texto.configure(text= "Vez do X")
            self.caixa_de_texto.configure(font= "Courie 10")
        jogo.recebe_jogada(2,2)
        self.botao_2_2.configure(state="disable")
        
        if jogo.verifica_ganhador() == 1:
            self.caixa_de_texto.configure(text= "X GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
        elif jogo.verifica_ganhador()==2:
            self.caixa_de_texto.configure(text= "O GANHOU")
            self.caixa_de_texto.configure(font= "Courie 10")
            self.reiniciar
            print("X Ganhou")
        elif jogo.verifica_ganhador() == 0:
            self.caixa_de_texto.configure(text= "DEU VELHA")
            self.caixa_de_texto.configure(font= "Courie 10")
            print("deu velha")
            self.reiniciar
        else:
            pass
        
    def iniciar(self):
        self.janela.mainloop()
        
    def reiniciar(self):
        jogo.limpa_jogadas()
        self.botao_0_0.configure(text= "")
        self.botao_0_0.configure(font = "Courie 10")                   
        self.botao_0_1.configure(text= "")
        self.botao_0_1.configure(font = "Courie 10")
        self.botao_0_2.configure(text= "")
        self.botao_0_2.configure(font = "Courie 10")
        self.botao_1_0.configure(text= "")
        self.botao_1_0.configure(font = "Courie 10")
        self.botao_1_1.configure(text= "")
        self.botao_1_1.configure(font = "Courie 10")
        self.botao_1_2.configure(text= "")
        self.botao_1_2.configure(font = "Courie 10")
        self.botao_2_0.configure(text= "")
        self.botao_2_0.configure(font = "Courie 10")
        self.botao_2_1.configure(text= "")
        self.botao_2_1.configure(font = "Courie 10")
        self.botao_2_2.configure(text= "")
        self.botao_2_2.configure(font = "Courie 10")
        self.caixa_de_texto.configure(text= "Vez do X")
        self.caixa_de_texto.configure(font= "Courie 10")
    
            
jogo_da_velha = Tabuleiro()
jogo_da_velha.iniciar()
