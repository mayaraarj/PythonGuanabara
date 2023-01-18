#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e se antecessor

numero =int(input("Digite um número inteiro: "))
sucessor = numero + 1
antecessor = numero -1

print('O sucessor do número digitado é {} e o antecessor é {}'.format(sucessor, antecessor))