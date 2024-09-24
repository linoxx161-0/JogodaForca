import random


#Criando a função do jogo
def game():
    print("\n Bem vindo ao Jogo da Forca!")
    print("Advinhe a palavra abaixo:\n")

    #Criando uma lista com as palavras do jogo
    palavras_possiveis = ["letra", "exibição", "lista", "espaço"]

    #Atribuindo uma palavra aleatória da lista de palavras possíveis à variável
    palavra = random.choice(palavras_possiveis)

    #List Comprehension atribuindo um underline para cada letra na variável palavra
    letras_adivinhadas = ["_" for letra in palavra]

    #Criar uma lista vazia para armazenar as letras erradas:
    letras_erradas = []

    #Definir o número máximo de chances:
    chances = 8

    while chances > 0:

        print(" ".join(letras_adivinhadas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        #Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        #Condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_adivinhadas[index] = letra
                index +=1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_adivinhadas:
            print("\nVocê venceu! A palavra era:", palavra)
            break
    if "_" in letras_adivinhadas:
        print("\nVocê perdeu! A palavra era: ", palavra )
        # Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")



