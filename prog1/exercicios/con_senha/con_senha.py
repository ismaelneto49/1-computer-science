senha = input()

senha_coded = f'{senha[0]}'
trocas = 0

for i in range(1, len(senha)):
    if(senha[i] == 'a'):
        senha_coded = f'{senha_coded}4'
        trocas+=1
    elif(senha[i] == 'e'):
        senha_coded = f'{senha_coded}3'
        trocas+=1
    elif(senha[i] == 'i'):
        senha_coded = f'{senha_coded}1'
        trocas+=1
    elif(senha[i] == 'o'):
        senha_coded = f'{senha_coded}0'
        trocas+=1
    else:
        senha_coded = f'{senha_coded}{senha[i]}'

print(f'{senha_coded} {trocas}(troca(s))')
