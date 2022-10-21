def subtrai_polinomios(p1, p2):
    resultado = []
    maior = list(p1)
    menor = list(p2)
    p1_menor = False

    if len(p1) < len(p2):
        maior = list(p2)
        menor = list(p1)
        p1_menor = True

    for i in range(len(maior) - len(menor)):
        menor.append(0)

    for j in range(len(menor)):
        if p1_menor:
            resultado.append(menor[j] - maior[j])
        else:
            resultado.append(maior[j] - menor[j])

    for k in range(len(resultado) - 1, -1, -1):
        if resultado[k] != 0: break
        resultado.pop(k)

    return resultado

