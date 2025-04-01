N = int(input())
sum_factorials = 0
factorial = 1

for i in range(N + 1):
    if i > 0:
        factorial *= i
    sum_factorials += 1 / factorial

print(f"{sum_factorials:.5f}")
