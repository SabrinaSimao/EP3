# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 00:11:46 2016

@author: sabri
"""

class Jogo:
    
    def __init__ (self):
        self.matriz_geral = [[0,0,0],[0,0,0],[0,0,0]]
        self.player = 1
        self.jogadas=0
        
    def recebe_jogada(self, linha, coluna):
        if self.player == 1:
            self.player = 9
        else:
            self.player = 1           
        self.matriz_geral[linha][coluna] = self.player
        
        #mudado na aula de DesSog quarta
        
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
        #Mudei o metodo de verificar empate
        self.jogadas+=1
        if self.jogadas==27:
            return 0

        return -1
               
            
    
    def limpa_jogadas(self):
        self.matriz_geral = [[0,0,0],[0,0,0],[0,0,0]]
        self.jogadas=0
        