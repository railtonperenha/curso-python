lp = float(input('A largura da parede é: '))
la = float(input('A altura da parede é: '))
ar = lp * la
tinta = ar / 2
print('A área da parede é {} m²'.format(ar))
print('Para pintar toda parede, será necessário {:.2f} litros de tinta'.format(tinta))

