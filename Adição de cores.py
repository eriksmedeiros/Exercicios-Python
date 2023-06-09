# Lista com as cores digitadas pelo usuário
rgb = []

# Solicita ao usuário as cores
vermelho = int(input("Digite 1 se o vermelho está presente, 0 caso contrário: "))
rgb.append(vermelho)

verde = int(input("Digite 1 se o verde está presente, 0 caso contrário: "))
rgb.append(verde)

azul = int(input("Digite 1 se o azul está presente, 0 caso contrário: "))
rgb.append(azul)

# Dicionario
cores = {
    'Preto' : [0, 0, 0],
    'Azul' : [0, 0, 1],
    'Verde' : [0, 1, 0],
    'Vermelho' : [1, 0, 0],
    'Ciano' : [0, 1, 1],
    'Amarelo' : [1, 1, 0],
    'Magenta' : [1, 0, 1],
    'Branco' : [1, 1, 1]
}

# Compara a lista rgb com o dicionário cores
for chave, valor in cores.items():
  if valor == rgb:
    print(chave)
  
input("Pressione Enter para sair...")