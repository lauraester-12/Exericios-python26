def nota_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3

    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    return f"Média: {media:.2f} - Situação: {situacao}"
not1 = float(input("Digite a primeira nota: "))
not2 = float(input("Digite a segunda nota: "))
not3 = float(input("Digite a terceira nota: "))
result = nota_media(not1, not2, not3)
print(result)