# Curso Python #06 - Tipos Primitivos e Saída de Dados

valor1 = input('Digite um valor: ')
valor2 = int(input('Digite um valor: '))
valor3 = float(input('Digite um valor: '))
valor4 = bool(input('Digite um valor: '))

print(type(valor1))
print(type(valor2))
print(type(valor3))
print(type(valor4))


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2

print(f'A soma entre {n1} e {n2} vale {s}')