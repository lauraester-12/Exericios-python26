M1 = int(input("Digite a idade da primeira mulher: "))
M2 = int(input("Digite a idade da segunda mulher: "))
H1 = int(input("Digite a idade do primeiro homem: "))
H2 = int(input("Digite a idade do segundo homem: "))
if (M1>M2):
    mv = M1
    mn = M2
else :
    mv = M2
    mn = M1
if (H1>H2):
    hv = H1
    hn = H2
else:
    hn = H1
    hv = H2
soma = hv + mn
mult= mv * hn

print ("A somda das idade é: ",soma)
print ("A multiplicação das idades é: ",mult)