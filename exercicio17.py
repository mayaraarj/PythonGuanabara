#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de 
#um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt

catetoOposto = float(input('Informe o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Informe o comprimento do cateto adjacente: '))

somaQuadradoCatetos = catetoOposto **2 + catetoAdjacente **2
hipotenusa = sqrt(somaQuadradoCatetos)

print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))