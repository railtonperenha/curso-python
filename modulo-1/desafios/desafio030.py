num = int(input('Digite um inteiro inteiro e descubra se ele é Par ou Ímpar: '))
print('Você digitou o número {}'.format(num))
if num % 2 == 0:
    print(num,':É um número Par')
else:
    print(num,':É um número Ímpar')