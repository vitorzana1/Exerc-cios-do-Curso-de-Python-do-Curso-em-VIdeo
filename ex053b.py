frase = str(input('Digite uma frase: ')).strip().upper()#.strip - > Tirou os espaços esternos e .upper() colocou tudo em maiusculo.
palavras = frase.split() #Separou a frase em lista
junto = ''.join(palavras) #dessa forma removeu os espçaos internos, mas se entre os '' tivesse * iria colocar no meio da frase
inverso = '' # atribuiu esse valor ao inverso de vazio
for letra in range(len(junto) -1, -1, -1): # len(junto) para saber a quantidade de letras da frase, -1 pois quer ir do final pro começo e -1 novamente pq quer ir descendo a frase
    inverso += junto[letra] # aqui ele recebe as letras do inverso a frente
if inverso == junto: # comparação
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo')