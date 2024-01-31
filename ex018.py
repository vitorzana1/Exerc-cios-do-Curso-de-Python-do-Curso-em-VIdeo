import math
ang = float(input('Digite o angulo que você deseja: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print('As medidas do angulo {} são SENO:{:.2f}, COSENO:{:.2f} e TANGENTE:{:.2f}'.format(ang,s, c, t))
