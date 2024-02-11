n = ''
s = 0
c = 0
while n != 999:
    n = int(input('Digite um número: (PARA SAIR DIGITE 999)'))
    if n != 999:
        s += n
        c += 1
print('A quantidade de números digitados foram {}'.format(c))
print('A soma dos números digitados é de {}'.format(s))

