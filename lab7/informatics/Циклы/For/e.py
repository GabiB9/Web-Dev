a = float(input())
n = int(input())

sum_gp = 0
current_term = 1

for i in range(n):
    sum_gp += current_term
    current_term *= a

print(sum_gp)
