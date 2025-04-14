# INSERINDO UM NOVO ELEMENO NO DICIONARIO

pessoas = {'Pedro': 18, 'Luana' : 20, 'Danilo' : 23} 

if pessoas.get('Danilo'):
  print('Pessoa existente')
else: 
  pessoas['Alicia'] = 36
  print(f'nova pessoa adicionada ao dicionario {pessoas}')

