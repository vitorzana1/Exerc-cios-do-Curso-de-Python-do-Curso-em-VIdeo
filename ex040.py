n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
if m >= 7:
    print('Parabéns! Sua média é {} e você foi\033[1m APROVADO!'.format(m))
elif m >= 5 and m < 7:
    print('Estude mais, sua média é {} e você está de\033[1m RECUPERAÇÃO!'.format(m))
else:
    print('Sua média é {} e você está\033[1m REPROVADO!'.format(m))
