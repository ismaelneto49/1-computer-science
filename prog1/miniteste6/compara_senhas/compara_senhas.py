def compara_senhas(senha1, senha2):
    tamanho = len(senha1)
    cont = 0
    if len(senha1) > len(senha2):
        tamanho = len(senha2)
    for i in range(tamanho):
        if senha1[i] != senha2[i]:
            cont+=1
    return cont

