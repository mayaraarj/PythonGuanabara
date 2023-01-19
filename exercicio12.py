#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço
# com 5% de desconto

precoOriginal=float(input('Digite o preço do produto: '))
novoPreco = 0.95 * precoOriginal

print('Com a aplicação do nosso desconto, seu produto agora sairá por {:.2f} reais.'.format(novoPreco))