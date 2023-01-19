#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela
# a sua porção inteira. Ex: O número 6.127 tem a parte inteira 6

import math

num = float(input('Digite um número real: '))
inteiro = math.trunc(num)

print('O numero {} tem a parte inteira {}'.format(num,inteiro))