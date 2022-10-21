# UFCG - prog1
# Ismael R. da Silva Neto
# calcula valor de comissao

vendedor = input("Qual é o nome do(a) vendedor(a)? ")
valor_venda = float(input("Qual é o valor da venda? "))

if valor_venda <= 500.00:
    comissao = valor_venda * 0.05
    print(f"O valor da comissão para o(a) vendedor(a) {vendedor} é R$ {comissao:.2f}.")
else:
    nome_monitor = f"{vendedor[0]}{vendedor[1]}{vendedor[2]}{vendedor[3]}{vendedor[4]}"
    comissao = valor_venda * 0.1
    print(f"O valor da comissão para o(a) vendedor(a) {nome_monitor} é R$ {comissao:.2f}.")
