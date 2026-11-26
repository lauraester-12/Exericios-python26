anonasc = int (input("Digite seu ano de nascimento: "))
anoatual = int (input("Digite o ano atual: "))
anoinicio = int (input("Digite seu ano de ingresso : "))
codigo = int (input("Digite seu codigo: "))
idade = anoatual - anonasc
tempoempresa = anoatual - anoinicio
print ("\nA idade do funcionário é: ",idade)
print ("\nO tempo de empresa do funcionário é: ",tempoempresa)
if ((idade >=65 or tempoempresa>=30) or (idade >=60 & tempoempresa >=25)):
    print ("\nRequer Aposentadoria")
else: 
    print ("\nNão requer aposentadoria\n")