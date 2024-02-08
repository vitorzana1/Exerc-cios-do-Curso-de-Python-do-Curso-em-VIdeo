from datetime import date
ma = 0
me = 0
for c in range(1,8):
    n = int(input('Digite o seu ano de nascimento: '))
    i = date.today().year - n
    atual = date.today().year
    print('A idade atual dessa pessoa é {} no ano de {}!'.format(i, atual))
    if i >= 21:
        ma += 1
    else:
        me += 1
print('Temos {} pessoas maiores de idade e {} menores de idade!'.format(ma,me))