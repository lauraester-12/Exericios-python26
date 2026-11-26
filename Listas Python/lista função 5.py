def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador
palavra = input("Digite uma palavra: ")
resultado = contar_vogais(palavra)
print("Quantidade de vogais:", resultado)