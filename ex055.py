ma = 0
me = 99999
for c in range(1,6):
    peso = float(input('Digite seu peso: '))

    if peso > ma:
        ma = peso
    elif peso < me:
        me = peso

print('O maior peso é {} e o menor é {}!'.format(ma, me))
