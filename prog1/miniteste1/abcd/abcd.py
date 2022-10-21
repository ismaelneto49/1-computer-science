# UFCG - prog1
# Ismael R. da Silva Neto
# calcula a expressao dc - a - b - ca - d + bb + aad

a = int(input())
b = int(input())
c = int(input())
d = int(input())

parte_dc = int(f"{d}{c}")
parte_ca = int(f"{c}{a}")
parte_bb = int(f"{b}{b}")
parte_aad = int(f"{a}{a}{d}")

expressao = parte_dc - a - b - parte_ca - d + parte_bb + parte_aad

print(expressao)
