# Desafio 019
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
# Correção

from random import choice

aluno1 = input('Informe o nome do(s) aluno(): ')
aluno2 = input('Informe o nome do(s) aluno(): ')
aluno3 = input('Informe o nome do(s) aluno(): ')
aluno4 = input('Informe o nome do(s) aluno(): ')

lista = [aluno1, aluno2, aluno3, aluno4]

sorteado = choice(lista)

print(f'O aluno escolhido foi {sorteado}')
