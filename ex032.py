ano = int(input('Digite um ano de sua escolha e veja se ele é bissexto: '))
novo = ano % 4 == 0 and ano%100!=0
print(novo)
if novo != 0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')
