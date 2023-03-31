dias = int(input('Por quantos dias você utilizou o carro ? '))
km = float(input('Quantos km você rodou com o carro ? '))
pago = (dias * 60) + (km * 0.15)
print('Você utílizou o carro por {} dias, e terá de pagar R$ {:.2f} à concessionária'.format(dias, pago))
