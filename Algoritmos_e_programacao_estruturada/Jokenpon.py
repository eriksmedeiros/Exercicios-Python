
import random

jogadas = ['Pedra', 'Papel', 'Tesoura']

modo = int(input('Digite \n1 para Rodada Única \n2 para Melhor de 5\n'))

# Rodada única
if modo == 1:
    computador = random.choice(jogadas)
    usuario = input('Pedra, Papel ou Tesoura? ')
    print(computador)
    print(usuario)
    
    if usuario == computador:
        print('empate')


    elif usuario == 'Papel' and computador == 'Tesoura':
        print('Computador winner')
    elif usuario == 'Papel' and computador == 'Pedra':
        print('Usuário Winner')

    elif usuario == 'Pedra' and computador == 'Tesoura':
        print('Usuário Winner')
    elif usuario == 'Pedra' and computador == 'Papel':
        print('Computador Winner')

    elif usuario == 'Tesoura' and computador == 'Pedra':
        print('Computador Winner')
    elif usuario == 'Tesoura' and computador == 'Papel':
        print('Usuário Winner')

    input("Pressione Enter para sair...")

# Melhor de 5
if modo == 2:

    usuario = 0

    for usuario in range(5):

        usuario = input('Pedra, Papel ou Tesoura? ')

        computador = random.choice(jogadas)

        if usuario == computador:
            print('empate')


        elif usuario == 'Papel' and computador == 'Tesoura':
            print('Computador winner')
        elif usuario == 'Papel' and computador == 'Pedra':
            print('Usuário Winner')

        elif usuario == 'Pedra' and computador == 'Tesoura':
            print('Usuário Winner')
        elif usuario == 'Pedra' and computador == 'Papel':
            print('Computador Winner')

        elif usuario == 'Tesoura' and computador == 'Pedra':
            print('Computador Winner')
        elif usuario == 'Tesoura' and computador == 'Papel':
            print('Usuário Winner')

    input("Pressione Enter para sair...")