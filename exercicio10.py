#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dólares ela pode comprar.

#considere 1 dolar = 3.27 reais

quantiaCarteira=float(input('Quantos reais você tem na sua carteira?'))
quantiaDolar = quantiaCarteira/3.27

print('Você poderá comprar {:.2f} dolares'.format(quantiaDolar))