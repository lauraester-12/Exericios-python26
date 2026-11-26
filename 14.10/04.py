quantidadeMO = float (input ("Digite a quantidade de morangos comprados: "))
if (quantidadeMO <= 5):
    morango = 2.50
else:
    morango = 2.20
quantidadeMA = float (input("Digite a quantidade de maçãs compradas: "))
if (quantidadeMA <= 5 ):
    maca = 1.80
else: 
    maca = 1.50

totalkg = (quantidadeMA + quantidadeMO)
valorf = (maca*quantidadeMA) + (morango*quantidadeMO)

if ( totalkg > 8 or valorf > 25):
    desconto = valorf*0.10
    valorc= valorf - desconto
else :
    valorc = valorf
print ("Valor a pagar: ",valorc)
print ("Total de morangos: ",quantidadeMO)
print ("Total de maçãs: ",quantidadeMA)