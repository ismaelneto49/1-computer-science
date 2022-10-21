def maior_slice(lista):
    
    slice = []
    for i in range(len(lista) - 1):
        if lista[i] < lista[i+1]:
            slice.append(lista[i])
        else:
            slice.append(lista[i])
            break

    return slice

print(maior_slice([7,6,2,9,10]))
