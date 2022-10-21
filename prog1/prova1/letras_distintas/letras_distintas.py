# UFCG - prog1 14/02/2022
# Ismael R. da Silva Neto 121111104
# Letras Distintas

word1 = input()
word2 = input()

count = 0
for i in word1:
    match = False
    for j in word2:
        if j == i:
            match = True
    if match:
        count +=1
    match = False

print(len(word1) - count)


