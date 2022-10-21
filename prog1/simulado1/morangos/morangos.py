# UFCG - prog1
# Ismael R. da Silva Neto
# Caixas de morangos

morangos = int(input())

caixas = morangos // 400
sobra = morangos % 400
percentagem = (sobra / morangos) * 100

print(f"{caixas} caixa(s) completa(s) para embalar os morangos.")
print(f"{percentagem:.1f}% dos morangos serão perdidos.")
