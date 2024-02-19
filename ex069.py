c = cm = cf = h = 0
while True:
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).strip().upper()
    f = ' '
    while f not in 'SN':
        f = str(input('Quer continuar? [S/N] ')).strip().upper()
    c += 1
    if i > 18:
        cm +=1
    if s == 'M':
        h += 1
    if s == 'F' and i < 20:
        cf += 1
    if f == 'N':
        break
print(f'Foram cadastrados {cm} pessoas com mais de 18 anos!')
print(f'Das {c} pessoas cadastradas, {h} são homens ', end='')
print(f'e {cf} são mulheres menores de 20 anos!')
