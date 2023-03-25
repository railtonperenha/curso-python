import random

print('Digite o nome dos alunos abaixo: ')
aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')
nomes = aluno1, aluno2, aluno3, aluno4
escolhidos1 = random.choices(nomes)
escolhidos2 = random.choices(nomes)
escolhidos3 = random.choices(nomes)
escolhidos4 = random.choices(nomes)
print('A ordem de apresentação dos alunos é: ')
print('1º {}'.format(escolhidos1))
print('2º {}'.format(escolhidos2))
print('3º {}'.format(escolhidos3))
print('4º {}'.format(escolhidos4))
