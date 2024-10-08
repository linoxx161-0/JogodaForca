
#Importação das bibliotecas random (para gerar palavras aleatórias) e os para a função limpar tela
from os import system, name
import random

#Função que irá limpar a tela sempre que o jogo reiniciar
def limpartela():
    if name = 'nt':
        _= system('cls') #comando para limpar no windows
    else:
        _=system(clear) #comando para limpar no MAC ou Linux

#Criação do Board(Tabuleiro). Cria uma lista com os itens que desenham o hangman
board = ["""

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========="""]

#Criação da classe principal HANGMAN, qual terá diversos métodos quais iremos utilizar para rodar o programa
class Hangman():
    def __init__(self, palavra): #Criação do método construtor que recebe como parametro palavra
        self.palavra = palavra   # e cria duas listas vazias para armarzenarmos as letras depois
        self.letras_erradas = []
        self.letras_escolhidas = []

    def guess(self, letra): #Criação do método para adivinhar a palavra
        if letra in self.palavra AND letra NOT in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)

        elif letra not in self.palavra and NOT in self.letras_erradas:
            self.letras_erradas.append(letra)

        else:
            return FALSE
        return TRUE

    def hangman_over(self): #método para verificar se o jogo acabou
        return self.hangman_won() or (len(self.letras) == 6)
    
    def hangman_won(self): #método para verificar se o jogador venceu
        if '_' NOT in self.hide_palavra():
            return TRUE 
        return FALSE

    def hide_palavra(self): #método para esconder a letra
        rtn = ''
        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += '_'
            else: 
                rtn += letra
        return rtn


    def print_game_status(self):

        print(board[len(self.letras_erradas)])
        print("\nPalavra: " + self.hide_palavra)
        print("\nLetras erradas: ",)

        for letra in self.letras_erradas:
            print(letra,)
            print()
            print("Letras corretas: ",)

            for letra in self.letras_escolhidas:
                print(letra,)
            print()

def main():

    limpartela()

    game = Hangman(rand.palavra())