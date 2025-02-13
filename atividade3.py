#Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar.

n1 = int(input("Digite um número inteiro : "))

if n1 %2 == 0:
    print(f"o numero {n1} é par")
else:
    print(f"O numero {n1} é impar")