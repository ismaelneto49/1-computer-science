limit = float(input())
level = float(input())

while True:
    if level >= limit: break
    event = input().split()

    if event[0] == 'chuva' or event[0] == 'afluente':
        level += float(event[1])
    if event[0] == 'demanda':
        if level - float(event[1]) > 0 and level < limit:
            level -= float(event[1])

print('Açude passou a liberar água.');
print(f'Nível: {level:.2f}')
