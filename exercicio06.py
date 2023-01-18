#Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e a sua raíz quadrada

numero = int(input("Digite um número: "))
dobro = 2 * numero
triplo = 3* numero
raizQuadrada = numero ** 0.5

print('O dobro do número digitado é {}, o seu triplo é {} e a sua raiz quadrada é {}'.format(dobro,triplo,raizQuadrada))