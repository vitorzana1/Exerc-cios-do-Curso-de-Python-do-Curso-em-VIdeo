t = int(input('Digite um número para ver sua taboada: '))
print('A taboada do número {} é:'.format(t))
for c in range( 1,11):
    print('{} x {} = {}'.format(c, t, c*t))