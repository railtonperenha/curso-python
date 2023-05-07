from time import sleep
from datetime import date
atual = date.today().year
nascimento = int(input('ANO DE NASCIMENTO: '))
print(f'VOCÊ NASCEU NO ANO DE {nascimento}')
idade = atual - nascimento
print(f'SUA IDADE É DE {idade} ANOS')

print()

print('-=-' * 10)
print('         CARREGANDO!    ')
print('-=-' * 10)
sleep(2)

print()

if idade == 18:
    print(f'VOCÊ DEVE SE ALISTAR ESSE ANO!')
elif idade < 18:
    saldo = 18 - idade
    print(f'FALTAM {saldo} ANOS PARA SE ALISTAR!')
    ano = atual + saldo
    print(f'SEU ALISTAMENTO SERÁ EM {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'VOCÊ DEVERIA TER SE ALISTADO A {saldo} ANOS')
    ano = atual - saldo
    print(f'SEU ALISTAMENTO FOI EM {ano}')
