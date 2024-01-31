salario = float(input('Digite o seu salario: '))
if salario > 1250:
    novo = salario * 1.10
    print('Seu novo salário é R$ {:.2f}'.format(novo))
else:
    novo = salario * 1.15
    print('Seu novo salário é R$ {:.2f}'.format(novo))