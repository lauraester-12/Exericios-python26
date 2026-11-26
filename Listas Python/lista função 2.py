def calcular_area_retangulo(largura, altura):
  return largura * altura
larg = float(input("Digite a largura do retângulo: "))
alt = float(input("Digite a altura do retângulo: "))

area = calcular_area_retangulo(larg, alt)
print(f"A área do retângulo é: {area}")
