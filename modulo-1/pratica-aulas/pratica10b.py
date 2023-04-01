'''n1 = float(input('Digite a primeira nota: '))
n2 = float (input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa. PARABÉNS!')
else:
    print('Sua média foi ruim. ESTUDE MAIS!')'''

n1 = float(input('Digite sua primeira nota: '))
n2 = float (input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
print('Sua média foi boa. PARABÉNS!' if m >= 6.0 else 'Sua média foi rui. ESTUDE MAIS!')
