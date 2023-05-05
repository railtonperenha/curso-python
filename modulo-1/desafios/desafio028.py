from random import randint
from time import sleep
computador = randint(0, 5)
print('Vou pensar em um número de 0 a 5, tente adivinhar qual é!')
jogador = int(input('Em qual número estou pensando agora ? '))
print('\033[34m-=-\033[m' * 15)
print('\033[33mPROCESSANDO! ... \033[m')
print('\033[34m-=-\033[m' * 15)
sleep(3)
if jogador == computador:
    print('\033[1;32m ACERTOU! Prabéns, você conseguiu me vencer!\033[m')
else:
    print(f'\033[1;31m ERROU! Pensei no número {computador} e não no número {jogador}. Tente novamente!\033[m')
