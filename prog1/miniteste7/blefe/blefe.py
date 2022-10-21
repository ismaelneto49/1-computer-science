def insert(array, index, element):
    for i in range(len(array)-1, index, -1):
        array[i] = array[i - 1]
    array[index] = element

def blefe(list):
    difference = len(list) * [None]
    if len(list) > 0:
        insert(difference, 0, 0)
    for i in range(len(list) - 1):
        if list[i] < list[i + 1]:
            insert(difference, i + 1, list[i + 1]-list[i])
            list[i + 1] = list[i]
        else:
            insert(difference, i+1, 0)
    return difference
