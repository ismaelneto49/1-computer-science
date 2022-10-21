# UFCG - prog1
# Ismael R. da Silva Neto
# Detector de ruídos

ruido = input()
hora = int(input())

if ruido != "" and (hora >= 22 or hora <= 6):
    print("Perturbação Detectada!")
else:
    print("Condomínio em Paz.")
