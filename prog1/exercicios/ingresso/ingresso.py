#UFCG - prog1
#Ismael R. da Silva Neto
#Calcula ingressos de cinema

quantidade_adultos = int(input())
quantidade_criancas = int(input())
preco_ingresso = float(input())

preco_total = quantidade_adultos * preco_ingresso + quantidade_criancas * (preco_ingresso / 2)

print(f"Total: R$ {preco_total:.2f}")
