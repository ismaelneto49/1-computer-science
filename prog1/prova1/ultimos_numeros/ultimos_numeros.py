# UFCG - prog1 14/02/2022
# Ismael R. da Silva Neto 121111104
# Somando os Ultimos Números

n = int(input())

sum_average = 0
numbers = []
for i in range(n):
    number = int(input())
    numbers.append(number)
    sum_average += number

average = 0
length = len(numbers)
if length != 0:
    average = sum_average / length

sum_last = 0
for j in range(1, length + 1):

    element = numbers[length - (length + j)]
    sum_last += element
    if element >= average: break

print(sum_last)


