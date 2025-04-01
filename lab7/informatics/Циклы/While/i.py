A = int(input())
a, b, n = 0, 1, 1
while b < A:
    a, b = b, a + b
    n += 1

if b == A:
    print(n)
else:
    print(-1)
