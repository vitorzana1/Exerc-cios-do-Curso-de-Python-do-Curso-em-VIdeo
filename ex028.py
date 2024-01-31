import random
num = int(input('Digite um número de 0 a 5: '))
sort = (random.randint(0,5))
if num == sort:
    print('Você acertou!')
else:
    print('Você errou! o número era {}'.format(sort))
