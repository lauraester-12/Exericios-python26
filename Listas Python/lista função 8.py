def somar_todos(*numeros):
    return sum(numeros)
entrada = input("Digite os números separados por espaço: ")
numeros = [float(n) for n in entrada.split()]
resultado = somar_todos(*numeros)
print("A soma total é:", resultado)