import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h = math.hypot(co,ca)
print(' O comprimento da hipotenusa é {:.2f}'.format(h))