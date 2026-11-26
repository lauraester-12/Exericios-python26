meses = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
temperaturas = []
stotal = 0

for i in range (12):
  temp = float(input(f"Digite a temperatura média de {meses[i]}: "))
  temperaturas.append(temp)
  stotal = stotal + temp
manual =  stotal/12
print (f"\nMédia anual das temperaturas: {manual:.2f}°C")
print ("\nMeses com a temperatura acima da média anual: ")
for i in range (12): 
  if temperaturas[i] > manual: 
    print (f"{i + 1} - {meses[i]}: {temperaturas[i]:.2f}°C")