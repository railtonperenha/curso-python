salario = float(input('Digite o valor do saláriom do funcionário desejado: R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('O salário do funcionário com aumento de 15% será de {:.2f}'.format(novo))
else:
    novo = salario + (salario * 10 / 100)
    print('O salário do funcionário com aumento de 10% será de {:.2f}'.format(novo))
 