#Crie um dicionário onde a chave seja uma tupla com o CPF do cliente e o valor seja uma lista 
# com seu nome e sua idade. Os dados deverão ser lidos pelo teclado. 
# No final, mostre o conteúdo do dicionário.


nome = dict()
cpf = tuple()
lista = list()

for i in range(3):
  cpf = int(input('CPF: '))
  nome = input('Nome: ')
  idade = int(input('Idade: '))
  nomes = [(cpf, )], [nome, idade]

print(nomes)