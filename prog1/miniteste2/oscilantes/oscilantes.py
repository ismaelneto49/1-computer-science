codigo = input()

validador = True

for i in range(len(codigo) - 1):

    atual = int(codigo[i])
    proximo = int(codigo[i + 1])

    if (atual % 2 == 0 and proximo % 2 == 0) or (atual % 2 != 0 and proximo % 2 != 0):
        validador = False

if validador:
    print(f"verdadeiro: {len(codigo)} algarismos.")
else:
    print(f"falso: {len(codigo)} algarismos.")
