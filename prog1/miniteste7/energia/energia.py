def calcula_conta(tabela):
    kwh = 0
    for l in range(1, len(tabela)):
        quantidade = tabela[l][1]
        tempo = tabela[l][2]
        watts = tabela[l][3]
        kwh += (quantidade * tempo * watts) / 1000
    reais = f'R$ {kwh * 0.28:.2f}'

    return reais
