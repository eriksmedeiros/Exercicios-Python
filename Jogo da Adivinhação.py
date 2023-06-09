# importando randint
from random import *

# selecione a dificudade
dificuldade = int(input('1 para Modo fácil e 2 para Modo difícil: '))

# modo fácil
if dificuldade == 1:
    numero = randint(1,31)
    print(numero)
    chute = 0
    for chute in range(5):
        chute = int(input('Adivinhe o número: '))
        if chute == numero:
            print('você acertou!')
            break
        elif chute < numero:
            print('o chute foi MENOR que o numero sorteado!')
        else:
            print('o chute foi MAIOR que o numero sorteado!')

    input("Pressione Enter para sair...")
    
# modo difícil
if dificuldade == 2:
    numero = randint(1,31)
    print(numero)
    chute = 0
    for i in range(1):
        chute = int(input('Adivinhe o número: '))
        if chute == numero:
            print('você acertou!')
        elif chute < numero:
            print('o chute foi MENOR que o numero sorteado!')
        else:
            print('o chute foi MAIOR que o numero sorteado!')

    input("Pressione Enter para sair...")
    