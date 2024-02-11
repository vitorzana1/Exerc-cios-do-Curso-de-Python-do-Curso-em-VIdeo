import math
num = ''
while num != 0:
    num = int(input('Digite um valor: (para sair digite 0) '))
    if num != 0:
        print('O número fatorial é de {} é {}'.format(num, math.factorial(num)))
print('FIM')
