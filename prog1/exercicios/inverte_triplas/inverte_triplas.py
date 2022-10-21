def inverte3a3(string):
    triples = []
    triple = ''
    for i in range(1, len(string)+1):
        triple = f'{triple}{string[i-1]}'
        if i % 3 == 0:
            triples.append(triple)
            triple = ''

    inverted = ''
    for j in range(len(triples) - 1, -1, -1):
        inverted = f'{inverted}{triples[j]}'

    return inverted
