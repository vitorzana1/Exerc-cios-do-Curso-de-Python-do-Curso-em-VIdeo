'''import random
num = int(input('Digite um número de 0 a 5: '))
sort = (random.randint(0,5))
if num == sort:
    print('Você acertou!')
else:
    print('Você errou! o número era {}'.format(sort))'''
#DESAFIO 28 ACIMA

from random import randint

pc = randint(0,10)
print(pc)
jogador = ''
c = 0

while pc != jogador:
    jogador = int(input('Adivinhe o número gerado pelo computador: '))
    c += 1
    if pc != jogador:
        print('Você errou, tente novamente!')
print('Você acertou! mas demorou {} vezes para acertar!'.format(pc, c))
