# Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

a = int(input("Digite um numero inteiro para representar a letra A: "))
b = int(input("Digite um numero inteiro para representar a letra B: "))

if a == b:
  print("Os numeros escolhidos são iguais")
elif a != b:
  print("Os numeros escolhidos são diferentes")
if a == b:
  c = (a + b)
  print("A soma dos numeros escolhidos é: ", c)
else:
  a != b
  c = (a * b)
  print("A multiplicacao dos numeros escolhidos é: ", c)
