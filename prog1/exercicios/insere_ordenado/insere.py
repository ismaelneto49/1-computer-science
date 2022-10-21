def insere_ordenado_primeiro(array):
    if array == []: return array

    element = array[0]
    for j in range(len(array)):
        for i in range(len(array) - 1 - j):
            if array[i] > array[i + 1]:
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
    return array
