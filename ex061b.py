'''i = int(input('Digite um número de ínicio: '))
p = int(input('Digite o número de alternancia de contagem: '))
for c in range(i, p*10, p):
    print(c)'''

print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')