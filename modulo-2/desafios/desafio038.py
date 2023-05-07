from time import sleep
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
print(f'Você digitou {num1} e {num2}')
sleep(2)
if num1 > num2:
    print('O primeiro valor é maior!')
elif num1 < num2:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')
