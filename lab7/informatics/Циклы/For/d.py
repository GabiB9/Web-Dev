import math

n = int(input())
k = int(input())

combinations = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
print(combinations)
