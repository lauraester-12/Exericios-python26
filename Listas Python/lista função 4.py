def maior_de_tres(a, b, c):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
resultado = maior_de_tres(num1, num2, num3)
print(f"O maior número digitado é: {resultado}")
