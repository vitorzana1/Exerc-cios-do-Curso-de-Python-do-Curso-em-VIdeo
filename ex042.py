a = float(input('Digite a medida da primeira reta: '))
b = float(input('Digite a medade da segunda reta: '))
c = float(input('Digite a medida da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('As suas medidas formam um triângulo')

    if a == b and b == c:
        print('O seu triângulo é\033[1m EQUILÁTERO\033[m!')
    elif a == b and b != c or b == c and c != a or c == a and a != b:
        print('O seu triângulo é\033[1m ISÓCELES\033[m!')
    elif a != b and b != c and c != a:
        print('O seu triângulo é\033[1m ESCALENO\033[m!')
else:
    print('Não é um triângulo!')

