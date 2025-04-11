#Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.

n1 = int(input("Digite um número inteiro e diferente do próximo: "))
n2 = int(input("Digite um número inteiro e diferente do próximo: "))
n3 = int(input("Digite um número inteiro e diferente do próximo: "))

lista = [n1, n2, n3]
lista.sort(reverse=True)
print (lista)