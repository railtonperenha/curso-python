import math
'''catb = float(input('Digite a medida do cateto oposto de um triângulo retângulo: '))
print('O valor do cateto oposto é {}'.format(catb))
catc = float(input('Digite o valor do cateto adjacente de um triângulo retângulo: '))
print('O valor do cateto adjacente é {}'.format(catc))
hip = math.sqrt(catb ** 2 + catc **2)
print('O valor da hipotenusa é {:.2f}'.format(hip))'''


co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))
