from random import randint
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei ? '))
if jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('Você errou, tente novamente!')
    