def remove_muitas_ocorrencias(lista):
    cont = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for e in lista:
        cont[e] += 1

    for i in range(len(cont)):
        if cont[i] >= 3:
            for indice in range(len(lista)-1, -1, -1):
                if lista[indice] == i:
                    lista.pop(indice)
