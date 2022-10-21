# UFCG - prog1
# Ismael R. da Silva Neto
# Calcula volume de uma piscina

comprimento = float(input())
largura = float(input())
profundidade = float(input())

volume_m3 = comprimento * largura * profundidade
volume_litros = volume_m3 * 1000

print(f"A piscina comporta {volume_litros:.2f} litros de água.")
