# UFCG - prog1
# Ismael R. da Silva Neto 121111104 
# Checa uma sequencia de digitos até que um dos criterios(6 impares, soma > limite, fim da sequencia) seja atingido

sequence = input()
limit = int(input())

to_print = 'final da sequência'
count_odd = 0
sum = 0
i = 0
while True:
    if count_odd == 6: 
        to_print = '6 ímpares'
        break
    if sum >= limit:
        to_print = 'limite'
        break

    if i != len(sequence):
        element = int(sequence[i])
        sum += element
        if element % 2 != 0: 
            count_odd += 1
    else: break
    i += 1

print(f'soma: {sum}')
if to_print == 'final da sequência':
    print(f'números lidos: {len(sequence)} de {len(sequence)}')
else:
    print(f'números lidos: {i} de {len(sequence)}')
print(f'critério de parada: {to_print}')

