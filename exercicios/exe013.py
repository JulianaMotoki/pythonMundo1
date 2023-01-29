# Desafio 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe seu salário atual: '))
aumento = salario * 0.15
salario_novo = salario + aumento

print(f'Seu salário passa de R${salario} para R${salario_novo}, um aumento de R${aumento}')