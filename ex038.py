primeiro = int(input('Digite um valor: '))
segundo = int(input('Digite outro valor: '))
if primeiro > segundo:
    print('O valor {} é maior que o valor {}'.format(primeiro, segundo))
elif segundo > primeiro:
    print('O valor {} é maior que o valor {}'.format(segundo, primeiro))
else:
    print('Os valores são iguais!')