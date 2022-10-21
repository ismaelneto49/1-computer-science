sequencia = input().split(' ')

cont = 0

for i in range(len(sequencia)-1):
    if (sequencia[i] == sequencia[i+1]):
        cont = cont + 1

print(cont)
