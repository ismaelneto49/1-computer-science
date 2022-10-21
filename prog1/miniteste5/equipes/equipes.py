to_print = 'Equipe Inválida'

count = 0
while True:
    name = input()
    if name == '-': break
    count += 1

if count == 11:
    to_print = 'Futebol'
if count == 7:
    to_print = 'Handebol'
if count == 6:
    to_print = 'Vôlei'
if count == 5:
    to_print = 'Basquete'

if to_print == 'Equipe Inválida':
    print(to_print)
else:
    print(f'Modalidade -> {to_print}')

