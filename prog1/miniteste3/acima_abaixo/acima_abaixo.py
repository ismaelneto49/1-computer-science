sum = 0
count = 0
values = []
while True:
    value = int(input())    
    if value < 0 or sum + value > 100: break
    
    values.append(value)
    sum += value
    count += 1

average = 0
if count != 0: 
    average = sum / count
for i in values:
    if i < average: 
        print(f'{i} < {average:.3f}')
    elif i > average:
        print(f'{i} > {average:.3f}')
