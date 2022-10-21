from functions import insertion_sort

#array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#array2 = [0, 10, 2, 3, 4, 5, 6, 7, 8, 9]

#print(insertion_sort(5, array2))

tupla1 = ("carlos", 18)

print(tupla1[0])

fila = [("a1", 10), ("a2", 15), ("a3", 20)]


def insere_na_fila(fila, nome, altura):
    aluno = (nome, altura)
    if fila == []:
        return fila
    trocas = False
    if not trocas:
        fila.append(aluno)
        for j in range(len(fila)):
            for i in range(len(fila) - 1 - j):
                if fila[i][1] > fila[i + 1][1]:
                    temp = fila[i + 1]
                    fila[i + 1] = fila[i]
                    fila[i] = temp
                    trocas = True
    return fila


print(insere_na_fila(fila, "a0", -18))
print(insere_na_fila(fila, "a5", 50))