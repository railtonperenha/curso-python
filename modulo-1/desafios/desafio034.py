salario = float(input('Digite aqui o slaário do funcionário desejado: R$ '))
if salario >= 1250:
    print('O salário do funcionário com aumento de 10% é de R$ {}'.format(salario * 1.10))
else:
    print('O salário do funcionário com aumento de 15% é de R$ {}'.format(salario * 1.15))
