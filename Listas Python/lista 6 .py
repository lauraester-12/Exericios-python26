cidades = ["Maracanaú", "Fortaleza", "Natal", "Madri", "Paris"]
busca = input("Digite o nome da cidade que deseja buscar: ")

if busca in cidades:
    posicao = cidades.index(busca)
    print(f"A cidade '{busca}' está na lista, na posição (índice) {posicao}.")
else:
    print(f"A cidade '{busca}' não está cadastrada na lista.")
