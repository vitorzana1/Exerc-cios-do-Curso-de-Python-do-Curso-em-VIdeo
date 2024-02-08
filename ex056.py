velho = 0
novo = 0
n = ''
s = ''
homem = 0
mulher = 0
anterior = 0
soma = 0
for c in range(1,5):
    print('---- PESSOA {}'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper()
    anterior = idade
    soma = soma + anterior  #media de idade
    if idade > velho: # Pessoa mais velha
        velho = idade
        n = nome
        s = sexo
    if sexo == 'M': # Contador de sexo
        homem = homem + 1
    else:
        mulher = mulher + 1

print(' A média de idade do grupo é de {} anos'.format(soma / 4))
if s == 'M':
    print('O homem mais velho tem {} anos e se chama {}'.format(velho, n))

else:
    print('A mulher mais velha tem {} anos e se chama {}'.format(velho, n))

print('A quantidade de homens é {} e a de mulheres é {}'.format(homem, mulher))


#minha compreesão do exercicio foi completamente diferente do proposto, no 56B estarei colocando a solução feita pelo proferssor, porém vou manter essa aqui para futuras analises e comparações
