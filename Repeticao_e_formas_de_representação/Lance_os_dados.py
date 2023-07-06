from random import randint

qtd_casas = int(input('Digite a quantidade de casas do tabuleiro: '))

def jogo_de_tabuleiro(qtd_casas):
  fabio = 0
  isabel = 0

  while True:
    input('É a vez de Fábio. Tecle Enter para jogar o dado. ')
    jogada_fabio = randint(1, 6)
    fabio += jogada_fabio
    print(f'Fabio lançou o dado e tirou: {jogada_fabio}' )
    if fabio >= qtd_casas:
      return 'Fábio ganhou!'
      break
    print(f'Posição atual de Fábio: {fabio}')

    input('É a vez de Isabel. Tecle Enter para jogar o dado. ')
    jogada_isabel = randint(1, 6)
    isabel += jogada_isabel
    print(f'Isabel lançou o dado e tirou: {jogada_isabel}')
    if isabel >= qtd_casas:
      return 'Isabel ganhou!'
      break
    print(f'Posição atual de Isabel: {isabel}')

jogo_de_tabuleiro(qtd_casas)
