numeros = []
par = []
for i in range (10):
    valor = float(input("Digite os números: "))
    numeros.append (valor)
for numero in numeros :
    if numero % 2 == 0:
        par.append (numero)
print (f"Lista original: {numeros} ")
print (f"Números Pares: {par}")
