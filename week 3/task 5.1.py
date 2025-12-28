def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

A, B = map(int, input().split())
C, D = map(int, input().split())

num = A*D - C*B
den = B*D

g = gcd(abs(num), den)
print(num // g, den // g)
