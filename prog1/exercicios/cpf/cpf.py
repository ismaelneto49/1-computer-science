def calcula_digitos_verificacao(cpf):
    digit1 = 0
    digit2 = 0
    
    multiplier = 2
    for i in range(len(cpf) - 1, -1, -1):
        element = int(cpf[i])
        digit1 += element * multiplier
        multiplier += 1
    
    digit1 = (10 * digit1) % 11
    if digit1 == 10:
        digit1 = 0

    cpf = f'{cpf}{digit1}'
    multiplier = 2
    for i in range(len(cpf) - 1, -1, -1):
        element = int(cpf[i])
        digit2 += element * multiplier
        multiplier += 1

    digit2 = (10 * digit2) % 11
    if digit2 == 10:
        digit2 = 0

    digits = f'{digit1}{digit2}'
    return digits
