imovel = float(input("Valor do imóvel R$ "))
salario = float(input("Salário do comprador R$ "))
tempo = int(input("Tempo de financiamento: "))
parcelas = imovel / (tempo * 12)
print(f"As parcelas do financiamento são de R$ {parcelas:.2f}")
if parcelas >= salario * 30 / 100:
    print("O valor das parcelas excedem à 30% do salário. Empréstimo NEGADO!")
else:
    print("O valor das parcelas representam menos que 30% do salário. Empréstimo APROVADO!")
