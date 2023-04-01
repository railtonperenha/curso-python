carro = float(input('Digite a velocidade que seu carro passou pelo radar: '))
print('Seu carro passou pelo radar com a velocidade de {} km/h'.format(carro))
multa = carro - 80
if carro > 80:
    print('Você passou acima do limite de velocidade. Terá de pagar uma multa de R$ {} pela infração cometida'.format(multa * 7))
else:
    print('Você respeitou as leis de transito. Parabéns!')
