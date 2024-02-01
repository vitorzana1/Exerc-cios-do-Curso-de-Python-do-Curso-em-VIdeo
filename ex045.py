from random import choice
jogador = int(input('Digite:\n 1 - PEDRA\n 2 - PAPEL\n 3 - TESOURA\n'))
lista = [1,2,3]
computador = choice(lista)
print(computador)
if jogador == 1 and computador == 1:
    print("Deu empate, ninguém ganhou!")
elif jogador == 1 and computador == 2:
    print('Eu joguei {}, ganhei de você!'.format(computador))
elif jogador == 1 and computador == 3:
    print('Eu joguei {} e você {}, você ganhou!'.format(computador,jogador))
elif jogador == 2 and computador == 1:
    print('eu joguei {}, você ganhou!'.format(computador))
elif jogador == 2 and computador == 2:
    print('Deu empate! ninguém ganhou!')
elif jogador == 2 and computador == 3:
    print('Ganhei! Eu joguei {} e você {}'.format(computador, jogador))
elif jogador == 3 and computador == 1:
    print('Eu ganhei! joguei {}'.format(computador))
elif jogador == 3 and computador == 2:
    print('Você ganhou pois jogou {} e eu {}!'.format(jogador,computador))
else:
    print('Deu empate! ninguém ganhou!')