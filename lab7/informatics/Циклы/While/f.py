x = float(input())
y = float(input())

day = 1
distance = x
while distance < y:
    day += 1
    distance *= 1.1

print(day)
