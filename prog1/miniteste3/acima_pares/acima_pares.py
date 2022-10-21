n = int(input())

sum = 0
count = 0
above = 0
values = []
for i in range(n):
    value = int(input())
    values.append(value)

    if value % 2 == 0:
        sum += value
        count += 1

average = sum / count

for j in values:
    if j > average:
        above += 1

print(f'média dos pares: {average}')
print(f'acima da média: {above}')
