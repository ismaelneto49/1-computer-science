# UFCG - prog1
# Ismael R. da Silva Neto
# Quadrado inscrito na circunferência

import math

lado = float(input())

raio = (lado * math.sqrt(2)) / 2
perimetro = 2 * math.pi * raio
area = math.pi * math.pow(raio, 2)

print(f"Perímetro: {perimetro:.5f}")
print(f"Área: {area:.5f}")
