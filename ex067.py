n = 0
c = 0
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    c = 0
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print('Obrigado por utilizar o programa de tabuadas!')
