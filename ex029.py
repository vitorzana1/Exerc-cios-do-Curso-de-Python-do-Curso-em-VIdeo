velocidade = int(input('Qual sua velocidade? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você ultrapassou o limite de velocidade e será multado em R${:.2f}'.format(multa))
