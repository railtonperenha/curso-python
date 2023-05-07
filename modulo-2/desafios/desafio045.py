from random import randint
from time import sleep
import emoji
itens = (emoji.emojize(':raised_fist:'), emoji.emojize(':hand_with_fingers_splayed:'), emoji.emojize(':victory_hand:'))
pc = randint(0, 2)
print('Suas Opções são:')
print(emoji.emojize('[ 0 ] PEDRA :raised_fist:'))
print(emoji.emojize('[ 1 ] PAPEL :hand_with_fingers_splayed:'))
print(emoji.emojize('[ 2 ] TESOURA :victory_hand:'))
jogada = int(input('Qual é a sua opção ? '))

print('-=' * 15)
print(f'O computador escolheu {itens[pc]}')
print(f'Você escolheu {itens[jogada]}')
print('-=' * 15)

sleep(2)

if pc == 0:
    if jogada == 0:
        print('EMPATE!')
    elif jogada == 1:
        print(f'JOGADOR GANHOU!')
    elif jogada == 2:
        print('PC GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 1:
    if jogada == 0:
        print('PC GANHOU!')
    elif jogada == 1:
        print('EMPATE!')
    elif jogada == 2:
        print(f'JOGADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 2:
    if jogada == 0:
        print(f'JOGADOR GANHOU!')
    elif jogada == 1:
        print('PC GANHOU!')
    elif jogada == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
