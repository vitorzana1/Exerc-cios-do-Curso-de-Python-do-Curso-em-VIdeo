s = 0
for c in range(0, 300):
    if c % 2 == 1 and c % 3 == 0:
        s += c
print('A soma de todos os números impares múltiplos de 3 é: {}'.format(s))