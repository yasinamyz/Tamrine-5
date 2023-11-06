import random

n = int(input("Enter n:"))
mine = []

for i in range(n):
    x = random.randint(1 , 100)
    if x not in mine:
        mine.append(x)

print(mine)





