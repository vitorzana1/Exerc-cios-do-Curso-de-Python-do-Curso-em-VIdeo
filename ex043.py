import time
tamanho = float(input('Qual a sua altura? (em CM)'))
peso = float(input('Qual o seu peso? '))
imc = (peso / (tamanho ** 2)) * 10000

if imc < 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.2f} e você está no seu peso IDEAL!'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {:.2f} e você está em SOBREPESO!'.format(imc))
elif imc > 30 and imc <= 40:
    print(' Seu IMC é {:.2f} e você está em OBESIDADE!'.format(imc))
else:
    print('Seu IMC é {:.2f} e você tem OBESIDADE MÓRBIDA!'.format(imc))
