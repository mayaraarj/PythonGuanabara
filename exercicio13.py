#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário
# com 15% de aumento

salarioAtual = float(input('Digite o salário atual: '))
novoSalario = salarioAtual * 1.15

print('O novo salário será de {:.2f} reais'.format(novoSalario))