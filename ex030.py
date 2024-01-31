num = float(input('Digite um número: '))
rest = (num % 2)
if rest == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))