import math

a1, b1 = map(float, input().split())
a2, b2 = map(float, input().split())

h1 = math.sqrt(a1*a1 + b1*b1)
h2 = math.sqrt(a2*a2 + b2*b2)

print(h1, h2)

if h1 > h2:
    print("First is bigger")
else:
    print("Second is bigger")
