# Desafio 020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import choices, shuffle

aluno1 = input('Informe o nome do(s) aluno(): ')
aluno2 = input('Informe o nome do(s) aluno(): ')
aluno3 = input('Informe o nome do(s) aluno(): ')
aluno4 = input('Informe o nome do(s) aluno(): ')

lista = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista)

print(f'A ordem de apresentação será \n{lista}')
