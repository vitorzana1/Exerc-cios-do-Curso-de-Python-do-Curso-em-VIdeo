import datetime
ano = int(input('digite seu ano de nascimento: '))
alistamento = (ano - datetime.date.today().year) * -1
tempo = (alistamento - 18) * -1
if alistamento < 18:
    print('Você ainda irá se alistar em {} anos.'.format(tempo))
elif alistamento == 18:
    print('Estamos no ano {} e você terá que se alistar!'.format(datetime.date.today().year))
else:
    print('Você tem {} anos, no ano de {} e seu tempo de se alistar já passou!'.format(alistamento,datetime.date.today().year))