#UFCG - prog1
#Ismael R. da Silva Neto
# Cálculo de Campos de Futebol

area1 = float(input())
area2 = float(input())
area3 = float(input())

campos1 = area1 / 4000.0
campos2 = area2 / 4000.0
campos3 = area3 / 4000.0
media = (campos1 + campos2 + campos3) / 3

print(f"{campos1:.2f}")
print(f"{campos2:.2f}")
print(f"{campos3:.2f}")
print(f"{media:.2f}")
