from random import shuffle
num = ['0', '1', '2', '3', '4', '5']
shuffle(num)
digite = print(input(str('Digite um número de 0 a 5 ')))
if digite == num:
    print('Você venceu!')
else:
    print('Você perdeu!')