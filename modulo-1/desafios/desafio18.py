import math
angulo = float(input('Digite o valor de um ângulo qualquer: '))
print('O ângulo em graus escolhido foi {}:'.format(angulo))
angulo_rad = math.radians(angulo)
print('O ângulo em radiano é {}'.format(angulo_rad))
sen = math.sin(angulo_rad)
cos = math.cos(angulo_rad)
tan = math.tan(angulo_rad)
print('O resultado de seno é {}, \nde cosseno {} \ne da tangente é {}'.format(sen, cos, math.ceil(tan)))
