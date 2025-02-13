#Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.

n1 = float(input("Digite um numero: "))

positivo = n1 > 0
negativo = n1 < 0

if positivo:
    dobro = n1 * 2
    print(f"O {n1} escolhido é um numero positivo")
    print("O seu dobro é : ", dobro)
elif negativo:
    triplo = n1 * 3
    print(f"O {n1} escolhido é um numero negativo")
    print("O seu triplo é :", triplo)
else:
    neutro = n1 == 0
    print("O numero escolhido é neutro", neutro)
