# contadores que vão ser utilizados posteriormente
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0

# escolha uma das opcoes
opcao = int(input("Escolha a opção: \n1 - Identifica intervalo \n2 - Calcular frequência de 30 notas: "))

# recebe uma nota e identifica a qual intervalo ela pertence.
if opcao == 1:

    numero = float(input('Nota: '))

    if 0 <= numero < 2.5:
        print('Grupo 1')
    if 2.5 <= numero < 5:
        print('Grupo 2')
    if 5 <= numero < 7.5:
        print('Grupo 3')
    if 7.5 <= numero <= 10:
        print('Grupo 4')

# recebe 30 notas de uma turma e calcula a frequência de notas em cada intervalo.
if opcao == 2:

    for nota in range(30):
        
        nota = float(input('Nota: '))

        if 0 <= nota < 2.5:
            cont1 += 1
        if 2.5 <= nota < 5:
            cont2 += 1
        if 5 <= nota < 7.5:
            cont3 += 1
        if 7.5 <= nota <= 10:
            cont4 += 1
    
    print(f'Grupo 1: {cont1} \nGrupo 2: {cont2} \nGrupo 3: {cont3} \nGrupo 4: {cont4}')