def cobrinha(matriz):
    snake = []
    change = False
    for l in range(len(matriz)):
        if not change:
            change = True
            for c in range(len(matriz[l])):
                e = matriz[l][c]
                if e % 2 != 0:
                    snake.append(e)
        else:
            change = False
            for c in range(len(matriz[l]) - 1, -1, -1):
                e = matriz[l][c]
                if e % 2 != 0:
                    snake.append(e)
    return snake

