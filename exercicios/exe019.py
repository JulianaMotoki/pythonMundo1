# Desafio 019
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import randint

aluno1 = input('Informe o nome do(s) aluno(): ')
aluno2 = input('Informe o nome do(s) aluno(): ')
aluno3 = input('Informe o nome do(s) aluno(): ')
aluno4 = input('Informe o nome do(s) aluno(): ')

sorteado = randint(1,6)

match (sorteado):
    case 1:
        print(aluno1)
    case 2:
        print(aluno2)
    case 3:
        print(aluno3)
    case 4:
        print(aluno4)
