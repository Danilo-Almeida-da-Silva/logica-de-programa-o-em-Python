#O IMC – Índice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / (altura) 2. Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo. IMC em adulta Condição Abaixo de 18,5 Abaixo do peso Entre 18,5 e 25 Peso normal Entre 25 e 30 Acima do peso Acima de 30 obeso.

nome = input("Digite seu nome: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc <= 18.5:
  print(f"{nome}, Você esta abaixo do peso e o seu IMC é de: {imc}")
elif imc > 18.5 and imc <= 25:
  print(f"Parabens {nome}, o seu peso esta normal e o seu IMC é de: {imc}")
elif imc > 25 and imc <= 30:
  print(f"{nome},Você esta acima do peso e o seu IMC é de: {imc}")
else:
  imc > 30
  print(f"{nome}, você esta com obesidade, procure um medico e nutricionista e seu imc é de: {imc}")
print("Obrigado por participar" ,nome)
