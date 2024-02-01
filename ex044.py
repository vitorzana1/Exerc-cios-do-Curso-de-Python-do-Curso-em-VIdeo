produto = float(input('Digite o valor do produto: '))
pagamento = int(input('Digite a forma de pagamento:\n 1 = Dinheiro \n 2 - PIX \n 3 - Cartão \n 4 - Cartão parcelado em até 2x \n 5 - Cartão parcelado em 3X ou mais\n'))
dinheiro = produto * 0.9
debito = produto * 0.95
credito = produto * 1.2
if pagamento == 1 or pagamento == 2:
    print('O preço a vista no dinheiro/pix do seu pagamento gerou um desconto! o preço do produto ficará: R${:.2f}'.format(dinheiro))
elif pagamento == 3:
    print('O pagamento no cartão de débito te dá um desconto! O preço do produto ficará: R${:.2f}'.format(debito))
elif pagamento == 5:
    print('O pagamento parcelado em 3x ou mais gera um valor extra sobre o produto, o valor ficará: R${:.2f}'.format(credito))
    parcelamento = int(input('Em quantas vezes você quer parcelar?'))
    novo = credito / parcelamento
    print('O Valor do produto ficará R${:.2f} e você pagaram em {}x. O valor da parcela é de R${:.2f}'.format(credito,parcelamento, novo))
else:
    print('O Produto em até 2x ficará no preço inicial de {:.2f}'.format(produto))
