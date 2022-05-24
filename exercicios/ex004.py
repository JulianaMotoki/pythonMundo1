# Desafio 004
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

tipo = input('Digite algo: ')
print('Qual é o tipo primitivo?')
print(type(tipo))

print('O valor digitado é do tipo numérico?')
print(tipo.isnumeric())

print('O valor digitado é uma letra?')
print(tipo.isalpha())

print('O valor digitado é do tipo alfanumérico?')
print(tipo.isalnum())

print('O valor digitado é composto somente por letras maiusculas?')
print(tipo.isupper())

print('O valor digitado é composto somente por letras minúsculas?')
print(tipo.islower())

print('O valor digitado é composto pelo menos por uma letra maiuscula?')
print(tipo.istitle())

print('A a string é vazia ou todos os caracteres na string são ASCII?')
print(tipo.isascii())


# Resolução

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())