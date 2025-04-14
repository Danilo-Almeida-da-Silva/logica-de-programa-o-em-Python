#carregando um vetor pelo teclado
import numpy as np

numeros = np.empty(5)#criar  um vetor vazio com 5(tamanho escolhido) index do tipo float

for i in range(5):
  numeros[i] = input('digite um numero: ')

print(numeros)