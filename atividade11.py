#Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de aproveitamento, usando a fórmula: MA := (nota1 + nota 2 * 2 + nota 3 * 3 + ME)/7 A atribuição dos conceitos obedece a tabela abaixo. O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a mensagem 'Aprovado' se o conceito for A, B ou C, e 'Reprovado' se o conceito for D ou E. Média de aproveitamento Conceito

#= 90 A >= 75 e < 90 B >= 60 e < 75 C >= 40 e < 60 D < 40 E


n1 = float(input("Digite a primeira nota de zero a cem: "))
n2 = float(input("Digite a segunda nota de zero a cem: "))
n3 = float(input("Digite a terceira nota de zero a cem: "))

me = (n1 + n2 + n3) / 3
ma = (n1 + n2 * 2 + n3 * 3 + me) / 7
a = me >= 90
b = me >= 75 and me < 90
c = me >= 60 and me < 75
d = me >= 40 and me < 60
e = me < 40

if ma == a:
  print("Você foi aprovado", ma)
elif ma == b:
  print("Aprovado", ma)
elif ma == c:
  print("Aprovado", ma)
elif ma == d:
  print("Reprovado", ma)
else:
  ma == e
  print("Reprovado", ma)