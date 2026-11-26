def exibir_perfil(nome, **dados_extras):
    print(f"O nome do usuário é {nome}")
    print(f"Os dados extras são {dados_extras}")

exibir_perfil(nome="Leticia", **{"cidade": "maracanau", "idade": 16})
