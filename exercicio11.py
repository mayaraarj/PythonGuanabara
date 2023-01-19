#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la
#sabendo que cada litro de tinta pinta uma área de 2 m**2

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
qntTinta = area/2

print('Você precisará de {} litros de tinta.'.format(qntTinta))
