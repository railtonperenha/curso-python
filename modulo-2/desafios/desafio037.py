num = int(input("DIGITE UM NÚMERO INTEIRO: "))
print('''ESCOLHA UMA DAS BASES PARA CONVERSÃO
[ 1 ] CONVERTER PARA BINÁRIO
[ 2 ] CONVERTER PARA OCTAL
[ 3 ] CONVERTER PARA HEXADECIMAL''')
opcao = int(input('DIGITE A OPÇÃO DESEJADA: '))
if opcao == 1:
    print(f'{num} CONVERTIDO PARA BINÁRIO É IGUAL A {bin(num) [2:]}')
elif opcao == 2:
    print(f'{num} CONVERTIDO PARA OCTAL É IGUAL A {oct(num) [2:]}')
elif opcao == 3:
    print(f'{num} CONVERTIDO PARA HEXADECIMAL É IGUAL A {hex(num) [2:]}')
else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE!')
