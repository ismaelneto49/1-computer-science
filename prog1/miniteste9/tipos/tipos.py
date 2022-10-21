def ordena_tipos(array):
    inteiros = []
    letras = []
    tipos = []

    for e in array:
        if e.isdigit():
            inteiros.append(e)
        elif e.isalpha():
            letras.append(e)
        else:
            tipos.append(e)

    final = []

    for n in inteiros:
        final.append(n)
    for l in letras:
        final.append(l)
    for t in tipos:
        final.append(t)

    return final


def test_1():
    a = ['1a', '2', 'e', '4', '4.4', 'e6', '8']
    assert ordena_tipos(a) == ['2', '4', '8', 'e', '1a', '4.4', 'e6']


def test_2():
    a = ['a', 'b', '1', '2', 'a1', 'a2', '1.0', '2.0']
    assert ordena_tipos(a) == ['1', '2', 'a', 'b', 'a1', 'a2', '1.0', '2.0']


def test_3():
    a = []
    assert ordena_tipos(a) == []


