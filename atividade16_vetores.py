#ARRAYS = VETORES/NUMPY
#VETORES NUMPY NÃO É LISTA
#sempre importar o numpy antes de usa-lo

import numpy as np

vetor = np.array([1, 2, 3, 4, 5, 6, 7])
type(vetor)

print(vetor.dtype) #retorna o tipo do vetor

vetor[0] = 100 #altera o valor do dado indicado do index
print(vetor)

vetorsoma = vetor + 10 #soma 10 em cada elemento
print(vetorsoma)

vetorMult = vetor * 2 #multiplica o elemento pela quantidade indicada
print(vetorMult)

print(sum(vetor)) #soma todos os elementos

print(min(vetor)) #mostrar o menor elemento

print(max(vetor)) #mostrar o maior elemento

print(len(vetor)) #retorna quantidade de elemento

print(vetor.mean()) #retorna a média dos valores