# Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).

nome = input("Digite o seu nome: ")
sexo = input("Digite seu sexo com apenas F ou M: ")
estadocivil = input("Você é uma pessoa CASADA(O) ou SOLTEIRA? : ")

if sexo == "M" and estadocivil == "SOLTEIRA":
    print("Seu sexo é: ", sexo)
    print("seu estado civil é: ", estadocivil)
elif sexo == "F" and estadocivil == "CASADA":
    tcasada = int(input("Qual o seu tempo de casada?: "))
    print("Seu tempo de compromisso é: ", tcasada)

print("seu nome é: ", nome)
print("seu sexo é :", sexo)
print("seu estado civil é: ", estadocivil)
