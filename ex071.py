valor = int(input('Qual valor a ser sacado? R$ '))
t = valor
c = 50
tc = 0
while True:
    if t >= c:
        t -= c
        tc += 1
    else:
        if tc > 0:
            print(f'Foram entregues {tc} notas de {c} reais')
        if c == 50:
            c = 20
            tc = 0
        elif c == 20:
            c = 10
            tc = 0
        elif c == 10:
            c = 1
            tc = 0
        if t == 0:
            break
print('OBRIGADO!')
