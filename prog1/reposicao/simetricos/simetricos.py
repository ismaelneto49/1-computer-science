# UFCG - prog1
# Ismael R. da Silva Neto 121111104
# Recebe uma lista e soma os valores em posições espelhadas

def soma_simetricos(lista):
    simetricos = []
    central = 'flag'
    if len(lista) % 2 != 0:
        central = lista[len(lista) // 2]
        for i in range(len(lista)):
            if lista[i] == central:
                lista.pop(i)
                break;

    for indice in range(len(lista) // 2):
        atual = lista[indice]
        oposto = lista[(indice + 1) * -1]
        soma = atual + oposto
        simetricos.append(soma)

    if central != 'flag':
        simetricos.append(central)
    
    return simetricos


def test_1():
    assert soma_simetricos([1, 2, 3, 4, 5]) == [6, 6, 3]


def test_2():
    assert soma_simetricos([2, 4, 6, 8]) == [10, 10]


def test_3():
    assert soma_simetricos([1]) == [1]


def test_4():
    assert soma_simetricos([]) == []


def test_5():
    assert soma_simetricos([15, 22, 95, 14, 0]) == [15, 36, 95]
