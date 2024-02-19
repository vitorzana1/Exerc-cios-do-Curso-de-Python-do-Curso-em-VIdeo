import random
c= 0
while True:
    pc = random.randint(0, 10)
    escolha = str(input('Você escolhe par ou impar? [P/I] ')).upper().strip()
    if escolha in 'IP':
        jogador = int(input('Escolha um número: '))
        soma = pc + jogador
        print(f'O jogador escolheu {jogador} e o computador {pc}, no total deu {soma}')
        if escolha == 'I':
            if soma % 2 == 0:
                break
            else:
                print('Você escolheu IMPAR e ganhou!\n Vamos jogar novamente...')
                c += 1
        if escolha == 'P':
            if soma % 2 == 1:
                break
            else:
                print('Você escolheu PAR e ganhou!\n Vamos jogar novamente...')
                c += 1
    else:
        print('Você não escolheu uma opção válida! Tente novamente.')
if c < 1:
    print(f'Você perdeu! Não ganhou nenhuma vez!')
elif c < 2:
    print(f'Você perdeu! Ganhou apenas {c} vez!')
else:
    print(f'Você perdeu! Ganhou {c} vezes')
