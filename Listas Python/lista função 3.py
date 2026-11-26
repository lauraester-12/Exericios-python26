def eh_par(numero):
  return numero % 2 == 0
num = int(input("Digite um número inteiro: "))
if eh_par(num):
  print(f"O número {num} é PAR.")
else:
  print(f"O número {num} é ÍMPAR.")
