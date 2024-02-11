n1 = int(input('Digite um número:'))
n2 = int(input('Digite o segundo número: '))
s = ''
menu = ''
while menu != 5:

    menu = int(input('Digite o número para executar a função:\n [1] SOMAR\n [2] MULTIPLICAR\n [3] MAIOR NÚMERO\n [4] NOVOS NÚMEROS\n [5] SAIR DO PROGRAMA\n Digite sua resposta: '))
    if menu == 1:
        s = n1 + n2
        print('A soma dos números é {}'.format(s))
    elif menu == 2:
        s = n1 * n2
        print('A multiplicação dos números é {}'.format(s))
    elif menu == 3:
        if n1 > n2:
            s = n1
            print('O maior número digitado foi: {}'.format(s))
        else:
            print('O maior número digitado foi {}'.format(n2))
    elif menu == 4:
        n1 = int(input('Digite um número:'))
        n2 = int(input('Digite o segundo número: '))

print('Obrigado por participar!')
