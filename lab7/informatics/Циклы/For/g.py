n = int(input())
sum_series = 0

for i in range(n + 1):
    sum_series += (-1)**i / (2 * i + 1)

result = 4 * sum_series
print(f"{result:.5f}")
