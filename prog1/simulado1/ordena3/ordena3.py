# UFCG - prog1
# Ismael R. da Silva Neto
# ordena entre 3 números inteiros

n1 = int(input())
n2 = int(input())
n3 = int(input())

maior = n1
meio = n2
menor = n3
# 10 10 10
if n1 >= n2 and n1 >= n3:
    maior = n1
    if n2 >= n3:
        meio = n2
        menor = n3
    elif n3 >= n2:
        meio = n3
        menor = n2
    print(f"{menor} {meio} {maior}")

elif n2 >= n1 and n2 >= n3:
    maior = n2
    if n1 >= n3:
        meio = n1
        menor = n3
    elif n3 >= n1:
        meio = n3
        menor = n1
    print(f"{menor} {meio} {maior}")

else:
    maior = n3
    if n1 >= n2:
        meio = n1
        menor = n2
    elif n2 >= n1:
        meio = n2
        menor = n1
    print(f"{menor} {meio} {maior}")
