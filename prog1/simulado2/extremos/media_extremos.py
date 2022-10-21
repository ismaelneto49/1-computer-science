n = int(input())

conjunto = []

for i in range(n):
    elemento = int(input())
    conjunto.append(elemento)

maior = conjunto[0]
menor = conjunto[0]
for a in range(len(conjunto)):
    if(conjunto[a] > maior):
        maior = conjunto[a]
    if(conjunto[a] < menor):
        menor = conjunto[a]

media_extremos = (maior + menor)/2

acima_media = 0
abaixo_media = 0

for b in range(len(conjunto)):
    if(conjunto[b] > media_extremos):
        acima_media += 1
    elif(conjunto[b] < media_extremos):
        abaixo_media += 1

print(f'Menor número: {menor}')
print(f'Maior número: {maior}')
print(f'Média dos extremos: {media_extremos:.2f}')
print(f'{abaixo_media} número(s) abaixo da média')
print(f'{acima_media} número(s) acima da média')
