# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 00:11:46 2016

@author: sabri
"""
matriz_geral = [[0,0,0],[0,0,0],[0,0,0]]

class Jogo:
    
    def __init__ (self, matriz_geral):
        self.matriz_geral = matriz_geral
        self.player1 = True
        self.player2 = False
        #alguem me salva com isso?!?! :(
        
    def recebe_jogada(self, linha, coluna):
        self.player2 ^= 1        
        self.player1 ^= 1
        
"""OK CLARAMENTE SE VE O PROBLEMA COM ESSE SWAP *se mata*
 Achei um legal na internet pra ficar flipando valores booleanos, vou dar commit nisso e atualizar depois
 Teoricamente, isso deve funcionar. Existem infinitos jeitos de fazer o swap, aqui vai o link por curiosidade:
 http://stackoverflow.com/questions/1779286/swapping-1-with-0-and-0-with-1-in-a-pythonic-way  """
        
        
    def verifica_ganhador(self):
        """nesta parte do codigo, vamos usar uma lógica que achei muito interessante na internet,
            que usa a soma de numeros de uma matriz para checar as linhas e colunas. 
            Dessa forma nao precisamos checar um por um"""
        #verificar as horizontais
        #NAO SE SABE AINDA SE O PRIMEIRO VAI SER A BOLA OU O X
        for i in range(0,3):
            if sum(self.matriz_geral[i])==27:
                return 1
            if sum(self.matriz_geral[i])==3:
                return 2
        #verificar as verticais
        self.matriz_transposta=[[row[i] for row in self.matriz_geral] for i in range(3)]
        for i in range(0,3):            
            if sum(self.matriz_transposta[i])==27:
                return 1
            if sum(self.matriz_transposta[i])==3:
                return 2
        #verificar as diagonais (nesse caso vamos um por um....)
        if self.matriz_geral[1][1]==9:
            if self.matriz_geral[0][0]==self.matriz_geral[1][1] and self.matriz_geral[2][2]==self.matriz_geral[1][1]:
                return 1
            if self.matriz_geral[0][2]==self.matriz_geral[1][1] and self.matriz_geral[2][0]==self.matriz_geral[1][1]:
                return 1
        if self.matriz_geral[1][1]==1:
            if self.matriz_geral[0][0]==self.matriz_geral[1][1] and self.matriz_geral[2][2]==self.matriz_geral[1][1]:
                return 2
            if self.matriz_geral[0][2]==self.matriz_geral[1][1] and self.matriz_geral[2][0]==self.matriz_geral[1][1]:
                return 2
        #verificar se empatou
        #usando a logica importada da internet, esse medoto soma todos os elementos da matriz, de forma que se o
        #resultado for 41, é empate (nota-se que o primeiro tem que ser o de valor 1, e o segundo jogador, o de valor 9)
        if 0 not in self.matriz_geral:
            a=0
            for i in range(0,3):
                a+= sum(self.matriz_geral[i])
            if a==41:
                return 0
        else:
            return -1