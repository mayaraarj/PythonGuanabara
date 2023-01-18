#Escreva um programa que leia um valor em metros e o exiba convertido em centrímetros
# e milímetros

valor = float(input('Digite o valor em metros para a conversão: '))
valorCentimetro = 100 * valor
valorMilimetro = 1000 * valor

print('{} metros equivale a {} centímetros e a {} milímetros'.format(valor,valorCentimetro, valorMilimetro))