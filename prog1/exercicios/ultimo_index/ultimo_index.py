def ultimo_indice(element, array):
    negative_index = -1
    for i in range(-1, ((len(array)+1) * -1), -1):
        if array[i] == element:
            negative_index = i
            index = len(array) + negative_index
            return index

    return negative_index
