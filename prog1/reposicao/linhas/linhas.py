# UFCG - prog1
# Ismael R. da Silva Neto 121111104
# Recebe sequências de números e avalia suas validades (válida se Npares > Ninpares)

numero_linha = 0
cont_invalidas = 0
while True:
    entrada = input()
    if entrada == 'fim': break
    
    valores = entrada.split()
    cont_pares = 0
    cont_impares = 0
    for v in valores:
        if int(v) % 2 == 0:
            cont_pares += 1
        else:
            cont_impares += 1
    
    numero_linha += 1
    if cont_impares > cont_pares:
        print(f'linha {numero_linha} inválida: {entrada}')
        cont_invalidas += 1

print(f'sequências lidas: {numero_linha} (inválidas: {cont_invalidas})')
