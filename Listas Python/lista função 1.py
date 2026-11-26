def saudar(nome, periodo="Bom dia"):
    periodo = periodo.lower()

    if periodo == "dia":
        print(f"Bom dia, {nome}!")
    elif periodo == "tarde":
        print(f"Boa tarde, {nome}!")
    elif periodo == "noite":
        print(f"Boa noite, {nome}!")
    else:
        print(f"Olá, {nome}! (Período inválido)")
saudar("Maria")  
saudar("João", "tarde") 
saudar("Ana", "noite")
