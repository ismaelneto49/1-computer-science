n = int(input())

dobradas = []
normais = []

cont = 0
letras_rep = 0
for i in range(n):
    palavra = input()

    for a in range(len(palavra)-1):
        if(letras_rep == 0):
            if(palavra[a] == palavra[a+1]):
                dobradas.append(palavra)
                cont = cont + 1
                letras_rep = letras_rep + 1
    if(cont == 0):
        if(palavra != ''):
            normais.append(palavra)
    cont = 0
    letras_rep = 0

print(f'{len(dobradas)} palavra(s) com letras dobradas:')
for b in range(len(dobradas)):
    print(dobradas[b])

print('---')

print(f'{len(normais)} palavra(s) sem letras dobradas:')
for c in range(len(normais)):
    print(normais[c])
