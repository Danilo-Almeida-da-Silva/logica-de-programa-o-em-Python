#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: ● para homens: (72.7 * h) – 58; ● para mulheres: (62.1 * h) – 44.7.

h = float(input("Digite sua altura: "))
sexo = input("Você é do sexo F ou M?: ")

men = (72.7*h) - 58
women = (62.1*h) - 44.7

if sexo == "F":
  women = (62.1*h) - 44.7
  print("seu peso ideal é: ",women)
else:
  sexo == "M"
  men = (72.7*h) - 58
  print("Seu peso ideal é: ",men)