def swap(e1, e2, array):
    index_e1 = 0
    index_e2 = 0

    for i in range(len(array)):
        if array[i] == e1:
            index_e1 = i
        if array[i] == e2:
            index_e2 = i
    array[index_e1] = e2
    array[index_e2] = e1


def idosos_inicio(fila):
    index_troca = 0
    for e in fila:
        if e >= 60:
            swap(e, fila[index_troca], fila)
            index_troca += 1


def test_1():
    fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
    idosos_inicio(fila)
    assert fila == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]


def test_2():
    fila = [25, 33, 50, 50, 35, 8, 12, 15, 22, 50, 50, 30, 34]
    idosos_inicio(fila)
    assert fila == [25, 33, 50, 50, 35, 8, 12, 15, 22, 50, 50, 30, 34]


def test_3():
    fila = []
    idosos_inicio(fila)
    assert fila == []


def test_4():
    fila = [61, 62, 63, 64, 65]
    idosos_inicio(fila)
    assert fila == [61, 62, 63, 64, 65]


def test_5():
    fila = [30, 61, 62, 63, 64]
    idosos_inicio(fila)
    assert fila == [61, 62, 63, 64, 30]

