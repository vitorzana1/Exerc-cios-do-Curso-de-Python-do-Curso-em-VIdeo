from datetime import date
ano = int(input('Digite seu ano de nascimento?' ))
idade = date.today().year - ano
if idade <= 9:
    print('Sua idade é {} e sua categoria é a MIRIM'.format(idade))
elif idade > 9 and idade < 15:
    print('Sua idade é {} e sua categoria é a INFANTIL'.format(idade))
elif idade > 14 and idade < 20:
    print('Sua idade é {} e sua categoria é a JUNIOR'.format(idade))
elif idade > 19 and idade < 26:
    print('Sua idade é {} e sua categoria é a SENIOR'.format(idade))
else:
    print('Sua idade é {} e sua categoria é a MASTER'.format(idade))