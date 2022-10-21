def swap(indice1, indice2, lista):
    temp = lista[indice2]
    lista[indice2] = lista[indice1]
    lista[indice1] = temp


def negativos_no_fim(lista):
    cont_negativos = 0
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] < 0:
            cont_negativos += 1
            swap(i, len(lista) - cont_negativos, lista)


lista = [12, -21, -35, 8, 12, 15]
assert negativos_no_fim(lista) == None
assert lista == [12, 12, 15, 8, -21, -35]