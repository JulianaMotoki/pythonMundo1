# Desafio 018
# Faça um programa que lia um ângulo qualquer e mostre na tela o valor do seno, cosseno e a tangente desse ângulo.

from math import sin, cos, tan

angulo = float(input('Informe o ângulo: '))

print('1 - Seno \n2 - Cosseno \n3 - Tangênte')
opcao = input('Informe o número da opção desejada: ')

if opcao == '1':
    print(f'O Seno do ângulo {angulo} é {sin(angulo)}')
elif opcao == '2':
    print(f'O Cosseno do ângulo {angulo} é {cos(angulo)}')
elif opcao == '3':
    print(f'A Tangente do ângulo {angulo} é {tan(angulo)}')
else:
    print('Opção Inválida')