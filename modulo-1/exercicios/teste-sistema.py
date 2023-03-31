codigo = str(input(('Código ')).strip()).upper()
cod = codigo.replace(' ', '')
if cod == '32208':
    print('AMORTECEDOR DIANTEIRO GOL/PARATI/SAVEIRO R$ 270,00')
elif cod == 'B47097':
    print('AMORTECEDOR TRASEIRO GOL/PARATI/VOYAGE BOLA/G5/G6 R$ 247,00')
elif cod == 'MP30088':
    print('AMORTECEDOR DIANTEIRO CORSA/CELTA/PRISMA R$ 349,00')
elif cod == 'F1':
    print('ÓLEO MOTOR MINERAL IPIRANGA 20W50 R$ 25,00')
elif cod == 'F45920':
    print('ROLAMENTO RODA GOL BOLA R$ 89,00')
elif cod == 'SYL1097':
    print('PASTILHA FREIO CORSA/CELTA/PRISMA R$ 37,50')
elif cod == 'CT874K3':
    print('KIT CORREIA DENTADA CORSA/CELTA/PRISMA TODOS R$ 130,00')
elif cod == '99999':
    des = (input('DESCRIÇÃO ')).upper()
    val = (input('VALOR R$'))
    print('{} R$ {:.2f}'.format(des, float(val)))
    