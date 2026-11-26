convidados = []

for i in range (3):
    nomes = str(input("Digite o nome dos convidados: "))
    convidados.append(nomes)
    
print (f"Lista original: {convidados}")
desistente = str(input("Digite o nome do convidado desistente: "))
convidados.remove (desistente)
print (f"Lista após desistência: {convidados}")