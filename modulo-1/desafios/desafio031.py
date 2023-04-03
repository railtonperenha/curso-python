viagem = float(input('Qual é a distância da sua viagem ? '))
print('Você está prestes a começar uma viagem de {} km'.format(viagem))
if viagem <= 200:
    print('Sua viagem custará R$ {:.2f}'.format(viagem * 0.45))
else:
    print('Sua viagem custará R$ {:.2f}'.format(viagem * 0.50))
