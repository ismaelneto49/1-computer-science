n = int(input())

values = []
for i in range(n):
    value = int(input())
    values.append(value)
print('---')
a = int(input())
b = int(input())

below = 0
between = 0
above = 0

for j in values:
    if j < a:
        below += 1
    elif j > a and j < b:
        between += 1
    elif j > b:
        above += 1

print(f'{below} antes')
print(f'{between} entre')
print(f'{above} depois')
