import random
aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')
nomes = aluno1, aluno2, aluno3, aluno4
print('Nome dos alunos escolhidos: \nAluno 1 {} \nAluno 2 {} \nAluno 3 {} \nAluno 4 {}'.format(aluno1, aluno2, aluno3, aluno4))
escolhido = random.choice(nomes)
print('O aluno (a) escolhido (a) foi {}'.format(escolhido))
