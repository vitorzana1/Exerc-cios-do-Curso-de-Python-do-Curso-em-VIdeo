casa = float(input('Qual o valor da casa desejada? R$ '))
salario = float(input('Qual o seu salário? R$ '))
tempo = int(input('Em quantos anos você deseja pagar?'))
limite = salario * 0.30
meses = tempo * 12
valor = casa / meses
if valor <= limite:
    print('O valor mensal da sua casa é de R${:.2f}, com seu salário você poderá comprar!'.format(valor))
else:
    print('Infelizmente você não pode financiar sua casa.')
