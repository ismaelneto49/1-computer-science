def maioridade_penal(string_names, string_ages):
    names = string_names.split()
    ages = string_ages.split()
    of_age = ''
    for i in range(len(ages)):
        if int(ages[i]) >= 18:
            of_age = f'{of_age} {names[i]}'
    
    formatted = ''
    for c in range(1, len(of_age)):
        formatted = f'{formatted}{of_age[c]}'

    return formatted
