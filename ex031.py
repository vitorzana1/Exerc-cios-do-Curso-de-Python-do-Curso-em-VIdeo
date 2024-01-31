viagem = int(input('Qual a distância da sua viagem? '))
if viagem > 200:
    mais = viagem * 0.45
    desc = viagem * 0.05
    print('Sua viagem é bem longa! Sua passagem custará R${} e você terá um desconto de R${}'.format(mais,desc))
else:
    menos = viagem * 0.5
    print('Sua viagem custará R${}'.format(menos))