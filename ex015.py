d = int(input('Qual a quantidade de dias que você precisará do carro?'))
km = float(input("Qual a quantidade de KM's rodados?"))
t = (d * 60) + (km * 0.15)
print('O valor a ser pago é de: R${:.2f} '.format(t))