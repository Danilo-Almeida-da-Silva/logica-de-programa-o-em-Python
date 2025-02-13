#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.

a = int(input("Digite um número inteiro: "))
b = int(input("Digite um número inteiro: "))
c = int(input("Digite um númerointeiro: "))

soma = (a+b)

print(f"A soma de {a}+{b} é: {soma} ")
if soma >= c:
    print(f"A soma de {a}+{b} é maior que: {soma}")
else:
    print(f"A soma de {a}+{b} é menor que: {soma} ")