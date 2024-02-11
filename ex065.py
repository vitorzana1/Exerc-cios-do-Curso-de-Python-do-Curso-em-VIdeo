n = s = c = me = ma = 0
p = ''

while p != 'N':
    n = int(input('Digite um número:'))
    c += 1
    s += n
    p = str(input('Você quer continuar? [S/N] ')).upper()
    if c == 1:
        ma = n
        me = n
    if ma < n:
        ma = n
    if me > n:
        me = n
print('A média dos valores digitado é: {}'.format( s/c ))
print('O menor número digitado é: {}'.format(me))
print('o maior número digitado é: {}'.format(ma))
