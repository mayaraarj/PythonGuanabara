# Escreva um programa que pergunte a quantidade de Km percorridos por um carro
#  alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km
#  rodado.

kmPercorridos = float(input('Quantos km foram percorridos? '))
diasAluguel = int(input('Por quantos dias o carro foi alugado? '))
precoTotal = 60 * diasAluguel + 0.15 * kmPercorridos

print('Você deverá pagar {:.2f} reais'.format(precoTotal))