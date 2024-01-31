import math
um = int(input('Digite um número: '))
dois = int(input('Digite um número: '))
tres = int(input('Digite um número: '))
if tres > dois:
    coringa = dois
    dois = tres
    tres = coringa
if dois > um:
    coringa = um
    um = dois
    dois = coringa
if tres > dois:
    coringa = dois
    dois = tres
    tres = coringa
    print('O maior número é {} e o menor é {}'.format(um, tres))

else:
    print('O maior número é {} e o menor é {}'.format(um, tres))