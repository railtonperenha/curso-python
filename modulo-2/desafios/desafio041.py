from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 20:
    print('Categoria: SÊNIOR')
elif idade > 20:
    print('Categoria: MASTER')
