num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

maior = num1
menor = num1

if num2 > maior:
    maio = num2
if num3 > maior:
    maior = num3

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print('O maior número é {}'.format(maior))
print(('O menor número é {}'.format(menor)))
