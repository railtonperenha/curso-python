nota1 = float(input('PRIMEIRA NOTA: '))
nota2 = float(input('SEGUNDA NOTA: '))
media = (nota1 + nota2) / 2
print(f'A SUA MÉDIA É DE {media}!')
if 7 > media >= 5:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO!')
elif media < 5:
    print('VOCÊ FOI REPROVADO!')
elif media > 7:
    print('VOCÊ FOI APROVADO!')