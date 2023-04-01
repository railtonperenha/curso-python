viagem = int(input('Você está indo viajar. Digite a distância (em km): '))
print('Você irá viajar uma distância de {} km'.format(viagem))
if viagem > 200:
    print('Sua viajem irá custar R$ {:.2f}'.format(viagem * 0.50))
else:
    print('Sua viajem irá custar R$ {:.2f}'.format(viagem * 0.45))
