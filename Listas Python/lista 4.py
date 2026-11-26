dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado","Domingo"]
temperaturas = []
stotal = 0

for i in range (7):
    temp = float(input(f"Digite a temperatura média de {dias[i]}: "))
    temperaturas.append (temp)
    stotal = stotal + temp

msemanal = stotal / 7
minimo = min(temperaturas)
maximo = max(temperaturas)

print (f"\nA Média das temperatura é: {msemanal:.2f}°C")
print (f"A temperatura máxima é: {maximo}°C")
print (f"A temperatura mínima é: {minimo}°C")

