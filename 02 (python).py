valor = int(input("Digite um número entre 1 e 10: "))
x = 1

while valor < 1 or valor > 10:
    valor = int (input("Número inválido! Digite um número entre 1 e 10: "))
while x <= 10:
    resultado = valor * x
    print(valor, " x ", x, " = ", resultado)
    x = x + 1