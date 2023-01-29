# Desafio 014
# Escreva um programa que converta uma temperatura digitada em °C e converta para °F

temp = float(input('Informe a temperatura: '))

c_f = round(((temp * (9/5)) + 32),2)
c_k = round((temp + 273.15),2)

f_c = round(((temp - 32) * (5/9)),2)
f_k = round(((temp - 32) * (5/9) + 273.15),2)

k_c = round((temp - 273.15),2)
k_f = round(((temp - 273.15) * (9/5) + 32),2)



print(f'{temp}°C equivale a {c_f}°F')
print(f'{temp}°C equivale a {c_k}°K')

print(f'{temp}°F equivale a {f_c}°C')
print(f'{temp}°F equivale a {f_k}°K')

print(f'{temp}°K equivale a {k_c}°C')
print(f'{temp}°K equivale a {k_f}°F')
