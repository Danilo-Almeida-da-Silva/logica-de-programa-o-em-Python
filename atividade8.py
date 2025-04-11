#Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação.

n1 = int(input("Digite um número: "))

par = n1 % 2 == 0
impar = n1 % 2 != 0

if par:
  somapar = (n1 + 5)
  print(f"O Número {n1} escolhido é par e a soma é: ", somapar)
else:
  n1 == impar
  somaimpar = (n1 + 8)
  print(f"O Número {n1} escolhido é impar e a soma é: ", somaimpar)