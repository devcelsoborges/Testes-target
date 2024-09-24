nome = str(input("Digite uma palavra: "))
quantidade = nome.lower().count("a")
if quantidade > 0:
    print(f"A letra 'a' aparece {quantidade} vez(es) na palavra {nome}.")
else:
    print(f"A letra 'a' não aparece na palavra {nome}.")