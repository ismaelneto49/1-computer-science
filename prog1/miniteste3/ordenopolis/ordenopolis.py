while True:
    name1 = input('nome 1? ')
    name2 = input('nome 2? ')
    name3 = input('nome 3? ')
    valid = 'invalid'
    print(name1 < name2)
    print(name2 < name3)
    if name1 < name2 and name2 < name3:
        valid = 'valid'
    
    for i in range(len(name1)):
        element = name1[i]
        for j in range(len(name1)):  
            if element == name1[j]:
                valid = 'invalid'
                break
    for i in range(len(name2)):
        element = name2[i]
        for j in range(len(name2)):
            if element == name2[j]:
                valid = 'invalid'
                break
    for i in range(len(name3)):
        element = name3[i]
        for j in range(len(name3)):
            if element == name3[j]:
                valid = 'invalid'
                break
    if valid == 'valid': break
    print('nomes inválidos: tente novamente')
