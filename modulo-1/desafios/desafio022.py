nome = str(input('Digite aqui seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Seu nome tem um total de {} letras'.format(len(nome) - nome.count(' ')))
nomesepar = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(nomesepar[0])))