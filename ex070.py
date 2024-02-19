c = t = cp = barato = 0
while True:
    n = str(input('Digite o nome do produto: ')).strip()
    p = float(input('Digite o preço do produto: R$ '))
    t += p
    c += 1
    if p > 1000:
        cp += 1
    if c == 1:
        pbarato = n
        barato = p
    if barato > p:
        pbarato = n
    f = ' '
    while f not in 'SN':
        f = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if f == 'N':
        break
print(f'O total gasto na compra foi R$ {t} ', end='')
print(f'e {cp} produtos custam mais de R$1000 reais.')
print(f'O produto mais barato comprado foi: {pbarato}')
