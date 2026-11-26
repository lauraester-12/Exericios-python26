def subt (valor, custo =0):
    return custo - valor
valor = float(input("Digite o valor que Carla Cristina tem: "))
custo = float(input("Digite o custo da compra: "))
resultado = subt(valor,custo)

if (custo>valor):
    print (f"Valor insuficiente. Ainda faltam R${resultado}")
else:
    print ("Compra bem sucedidada.")