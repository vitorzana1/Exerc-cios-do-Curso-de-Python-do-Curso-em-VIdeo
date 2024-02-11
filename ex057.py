sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: (M para masculino e F para feminino)')).upper()
    if sexo != 'F' and sexo != 'M':
        print('Você digitou errado, tente novamente!')
if sexo == 'M':
    print('Você é do sexo masculino!')
else:
    print('Você é do sexo feminino!')
