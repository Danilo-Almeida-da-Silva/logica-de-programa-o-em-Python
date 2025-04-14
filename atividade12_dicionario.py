#Cadastre em um dicionário 5 produtos e seus respectivos preços, depois mostre o conteúdo do dicionário com um produto por linha.

produto = []

for i in range(5):
  nome = {}
  nome['nome'] = input('nome: ')
  nome['preço'] = float(input('Valor: '))
  produto.append(nome)

print(f'{produto}')

