# UFCG - prog1
# Ismael R. da Silva Neto
# recorde da carne de sol de picui

recorde_atual = float(input())
quantidade_comida = float(input())

if(quantidade_comida == recorde_atual):
    print("recorde empatado")
elif(quantidade_comida > recorde_atual):
    print(f"recorde quebrado ({quantidade_comida} kg)")
else:
    print("recorde mantido")
