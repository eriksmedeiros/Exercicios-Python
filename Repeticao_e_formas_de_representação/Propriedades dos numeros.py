primos = []

num = int(input('Digite um número inteiro para identificar os múltiplos de 6: '))

num += 1
multiplo = 1

for num in range(num-1):
    multiplo = num * 6
    print(multiplo)

print('O próximo múltiplo será:', multiplo + 6)

num = int(input('Digite um número inteiro para identificar se é primo ou composto: '))
for i in range(num+1):
    i += 1
    if num%i == 0:
        primos.append(i)
if primos == [1, num]:
    print(num, 'é primo')
else:
    print(num, 'é composto')

input("Pressione Enter para sair...")