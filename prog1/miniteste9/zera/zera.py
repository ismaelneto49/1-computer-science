def zera_nao_nulos(m, l, c):

    for i in range(c, len(m)):
        if m[l][i] != 0:
            m[l][i] = 0
        else: 
            break

    for i in range(c-1, -1, -1):
        if c-1 < 0: break

        if m[l][i] != 0:
            m[l][i] = 0
        else: break

    for i in range(l, len(m)):
        if m[i][c] != 0:
            m[i][c] = 0
        else:
            break

    for i in range(l-1, -1, -1):
        if l-1 < 0: break
        if m[i][c] != 0:
            m[i][c] = 0
        else: break


jogo = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
       ]    

zera_nao_nulos(jogo, 3, 2)

for e in jogo:
    print(e)



