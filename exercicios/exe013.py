# Desafio 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# Acrescentando o R$ para evitar que o usuário insira essa informação
# Também acrescentando a formatação de 2 casas decimais por ser um valor referente a dinheiro

salario = float(input('Informe seu salário atual: R$'))
aumento = salario * 0.15
salario_novo = salario + aumento

print(f'Seu salário passa de R${salario:.2f} para R${salario_novo:.2f}, um aumento de R${aumento:.2f}')