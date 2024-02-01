numero = int(input('Digite um número para conversão: '))
opcao = int(input('Digite a opção desejada:\n 1 - BINARIO\n 2 - Octal\n 3 - Hexadecimal'))
binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexa = hex(numero)[2:]
if opcao == 1:
    print('O número {} em Binário é {}'.format(numero,binario))
elif opcao == 2:
    print('O número {} em OCTAL é {}'.format(numero,octal))
elif opcao == 3:
    print('O número {} em hexadecimal é {}'.format(numero,hexa))
else:
    print('Número invalido!')
