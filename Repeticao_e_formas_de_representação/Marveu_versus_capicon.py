def encontre_mínimo(lista):
    return min(numeros)

def encontre_máximo(lista):
    return max(numeros)

def momento_mínimo_informado(lista):
    for indice, valor in enumerate(numeros):
        indice += 1
        if valor == min(numeros):
            return indice
        
def momento_máximo_informado(lista):
    for indice, valor in enumerate(numeros):
        indice += 1
        if valor == max(numeros):
            return indice
        
def somatório(lista):
    return sum(numeros)

def produtório(lista):
  produto = 1  
  for i in numeros:  
    produto *= i
  return produto

def média(lista):
    return sum(numeros)/10

def mediana(lista):
    numeros.sort()
    med = []
    for indice, valor in enumerate(numeros):
        indice += 1
        if indice == 5:
            med.append(valor)
        if indice == 6:
            med.append(valor)
    return sum(med)/2

def numeros_primos(numero):
  primos = []
  for i in range(numero+1):
    i += 1
    if numero%i == 0:
        primos.append(i)
  if primos == [1, numero]:
    return True
  return False

def todos_primos(lista):
  for i in numeros:
    if not numeros_primos(i):
      return False
  return True

def algum_primo(lista):
  for i in numeros:
    if numeros_primos(i):
      return True
  return False

numeros = []

for i in range(10):
   num = int(input('Digite um número: '))
   numeros.append(num)

print('Mínimo:', encontre_mínimo(numeros))
print('Máximo:', encontre_máximo(numeros))

print('Momento do mínimo:', momento_mínimo_informado(numeros))
print('Momento do máximo:', momento_máximo_informado(numeros))

print('Somatório:', somatório(numeros))
print('Produtório:', produtório(numeros))

print('Média:', média(numeros))
print('Mediana:', mediana(numeros))

print('Todos os números são primos:', todos_primos(numeros))
print('Tem algum número primo:', algum_primo(numeros))