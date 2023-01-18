#Faça um programa que leia algo pelo teclado e mostre na tela 
# o seu tipo primitivo e todas as informações possíveis sobre ele.

entrada = input("Digite algo: ")

print(type(entrada))
print(entrada.isalnum())
print(entrada.isalpha())
print(entrada.isdecimal())
print(entrada.isascii())
print(entrada.isidentifier())
print(entrada.isdigit())
print(entrada.islower())
print(entrada.isnumeric())
print(entrada.isupper())
print(entrada.istitle())
print(entrada.isspace())