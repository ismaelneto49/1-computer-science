def swap(i1, i2, array):
    temp = array[i1]
    array[i1] = array[i2]
    array[i2] = temp


def organiza_pedido(array):
    count_p = 0
    count_s = 0
    for e in array:
        if e == 'p':
            count_p += 1
        if e == 's':
            count_s += 1

    for j in range(count_p):
        for i in range(len(array)-1):
            if array[i] == 'p':
                swap(i, i+1, array)

    for j in range(count_s):
        for i in range(len(array)-1):
            if array[i] == 's':
                swap(i, i+1, array)


def test_1():
    l = ['s', 'd', 'd', 'p', 's', 'd', 's']
    assert organiza_pedido(l) == None
    assert l == ['d', 'd', 'd', 'p', 's', 's', 's']


def test_2():
    l = ['p', 's', 'd']
    assert organiza_pedido(l) == None
    assert l == ['d', 'p', 's']


def test_3():
    l = []
    assert organiza_pedido(l) == None
    assert l == []


def test_4():
    l = ['d', 'd', 'd', 'p', 'p', 'p', 's', 's', 's']
    assert organiza_pedido(l) == None
    assert l == ['d', 'd', 'd', 'p', 'p', 'p', 's', 's', 's']


