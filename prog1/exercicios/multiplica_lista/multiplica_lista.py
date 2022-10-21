def multiplica_lista(n, list):
    if n <= 0: return []

    multiplied = list + []
    for j in range(n-1):
        for i in range(len(list)):
            multiplied.append(list[i])

    return multiplied
