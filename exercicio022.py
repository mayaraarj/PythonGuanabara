#Crie um programa que leia o nome completo de uma pessoa e mostre:
nomeCompleto = str(input("Digite o nome completo: ")).strip()

# # 1) O nome com todas as letras maiúsculas
print(nomeCompleto.upper())

# # 2)O nome com todas minúsculas
print(nomeCompleto.lower())

# # 3)Quantas letras ao todo (sem considerar espaços)
qntsLetrasTodo = ''.join(nomeCompleto.split())
print(len(qntsLetrasTodo))


# # 4)Quantas letras tem o primeiro nome
fatiando = nomeCompleto.split()
primeiroNome = fatiando[0]
print(primeiroNome)
quantidadeLetras = len(primeiroNome)
print(quantidadeLetras)