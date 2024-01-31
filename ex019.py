import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluino: ')
lista = [a1, a2, a3, a4]
s = random.choice(lista)
print('O aluno escolhido foi {}'.format(s))