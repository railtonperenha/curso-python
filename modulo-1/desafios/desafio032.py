ano = int(input('Digite um ano e descubra se é um ano Bissexto: '))
print('Você escolheu o ano de {}'.format(ano))
if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
    print('O ano de {} é um ano Bissexto'.format(ano))
else:
    print('O ano de {} não é um ano Bissexto'.format(ano))
