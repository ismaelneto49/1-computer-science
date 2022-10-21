n = int(input())

maiores = 0;
quant_maiores = 0;

areas = []

for i in range(n):
    lados = input().split(" ")

    for a in range(len(lados)):
        lados[a] = float(lados[a])

    semiperimetro = (lados[0] + lados[1] + lados[2]) / 2
    
    area = (semiperimetro * (semiperimetro - lados[0]) * (semiperimetro - lados[1]) * (semiperimetro - lados[2])) ** 0.5
    areas.append(area)

    if area > 100:
        maiores += area
        quant_maiores += 1

area_maiores = 0

for j in range(len(areas)):
    print(f"Área {j + 1}: {areas[j]:.2f}")

if quant_maiores != 0:
    area_maiores = maiores / quant_maiores

print(f"Número maiores: {quant_maiores}, área média: {area_maiores:.2f}")

