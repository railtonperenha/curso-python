produto = float(input('Valor do Produto R$ '))
din = produto * 10 / 100
debito = produto * 5 / 100
parcelado = produto * 20 / 100
pagamento = int(input('''Formas de Pagamentos:
 [ 1 ] DINHEIRO/CHEQUE COM 10% DE DESCONTO
 [ 2 ] DÉBITO COM 5% DE DESCONTO
 [ 3 ] CRÉDITO ATÉ 2X SEM JUROS
 [ 4 ] CRÉDITO ACIMA DE 3X COM JUROS DE 20%
 ESCOLHA DAS FORMAS DE PAGAMENTO: '''))
if pagamento == 1:
    print(f'Sua compra custará R$ {produto - din:.2f} para pagamento no DINHEIRO/CHEQUE')
elif pagamento == 2:
    print(f'Sua compra custará {produto - debito:.2f} para pagamento no DÉBITO')
elif pagamento == 3:
    parcelas = int(input('Quantas parcelas ? '))
    if parcelas == 1:
        print(f'Sua compra custará {produto:.2f} para pagamento no CRÉDITO À VISTA')
    elif parcelas == 2:
        final = produto / parcelas
        print(f'''Sua compra será parcelada em {parcelas}x de R$ {final:.2f} SEM JUROS!
Sua compra custará {produto:.2f} no final''')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas ? '))
    juros = produto / parcelas * 20 / 100
    final = juros + produto / parcelas
    total = final * parcelas
    print(f'''Sua compra será parcelada em {parcelas}x de R$ {final:.2f} COM JUROS DE 20%.
Sua compra de R$ {produto:.2f} custará {total:.2f} no final''')
