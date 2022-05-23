n = float(input('Digite um valor: '))
print(n)


# Métodos de Teste de Tipos
n = input('Digite algo: ')
print(n.isnumeric()) # Verifica se o que foi digitado é ou não numérico e retorna True ou False
print(n.isalpha()) # Verifica se o que foi digitado é ou não letra e retorna True ou False
print(n.isalnum()) # Verifica se o que foi digitado é ou não alfanumérico e retorna True ou False
print(n.isupper()) # Verifica se o que foi digitado está somente com letras maiusculas e retorna True ou False