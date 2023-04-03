carro = float(input('Qual é a velocidade atual do carro ? '))
print('Seu carro passou pelo radar com a velocidade de {} km/h'.format(carro))
multa = (carro - 80) * 7
if carro > 80:
    print('MULTADO!! Terá de pagar uma multa de R$ {:.2f} pela infração cometida'.format(multa))
print('Você respeitou as leis de transito. Parabéns!')
