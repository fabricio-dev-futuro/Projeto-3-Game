# Versão 1 do jogo:

# Pacote que faz seleção aleatória 
import random
from os import system, name


def limpa_tela():
    if name == 'nt':

        _= system('cls')        
    else:
        _= system('clear')

# Função
def jogo():
    limpa_tela()
    print('\nAdivinhe a palavra abaixo:\n')

    # Lista de palavras
    my_palavras = [
        'adidas', 'nike', 'prada', 'gucci', 'puma', 'ellus',
        'reserva', 'toyota', 'ford', 'nissan', 'tesla', 'honda',
        'samsung', 'apple', 'xiaomi', 'sony', 'acer', 'mancer',
        'pichau', 'lenovo', 'umbro', 'vans', 'redley' 
        ]

    
    my_palavra = random.choice(my_palavras)


    
    my_letras_descobertas = ['*' for letra in my_palavra]

    # Numero de chances
    my_chances = 9

    # Lista para as letras erradas
    my_letras_erradas = []

    # Loop enquanto o número de chances for maior do que zero
    while my_chances > 0:

        # Preenchimento do jogo:
        # O uso o join faz a junção da esquerda com a direita
        print(' '.join(my_letras_descobertas))
        print('\n Chances restantes:', my_chances)
        print('Letras erradas:', ' '.join(my_letras_erradas))

    # Tentativa
        my_tentativa = input('\nDigite uma letra: ').lower()

    # Condicional
        if my_tentativa in my_palavra:
            index = 0

            for letra in my_palavra:
                if my_tentativa == letra:
                    my_letras_descobertas[index] = letra
                index += 1
        else:
            my_chances -= 1
            my_letras_erradas.append(my_tentativa)
        

        # Checagem do processo (versão vencedora)
        if '*' not in my_letras_descobertas:
            print('\nVocê venceu, a palavra era:', my_palavra)
            break

    
    # Checagem do processo (versão perdedora)
    if '*' in my_letras_descobertas:
        print('\nVocê perdeu, a palavra era:', my_palavra)



# Indicando que esse módulo é um programa python (uso do Bloco main)
if __name__ == '__main__':
    jogo()