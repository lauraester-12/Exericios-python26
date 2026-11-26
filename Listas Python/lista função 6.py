def filtrar_pares(lista_numeros):
    pares = []

    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares
numeros = input("Digite vários números inteiros separados por espaço: ")
lista_numeros = [int(numero) for numero in numeros.split()]
resultado = filtrar_pares(lista_numeros)
print("Números pares:", resultado)