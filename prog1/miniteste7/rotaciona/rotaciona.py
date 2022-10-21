def rotesq(array):
    for i in range(len(array)-1):
        temp = array[i]
        array[i] = array[i + 1]
        array[i + 1] = temp
