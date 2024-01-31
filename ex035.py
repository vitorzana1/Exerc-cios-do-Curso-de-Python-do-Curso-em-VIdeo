um = int(input('Digite a medida da primeira reta: '))
dois = int(input('Digite a medida da segunda reta: '))
tres = int(input('Digite a medida da tericeira reta: '))
teste = um + dois
print(teste)
if teste > tres:
    print('Suas medidas formam um triângulo')
else:
    print('As medidas não formam um triângulo.')