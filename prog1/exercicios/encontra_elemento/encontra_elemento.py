# UFCG - prog1
# Ismael R. da Silva Neto
# Encontrar elemento em uma sequência de inteiros

numero = int(input())
sequencia = input().split()

printar = "não"

for i in sequencia:
    if(numero == int(i)):
        printar = "sim"

print(printar)
