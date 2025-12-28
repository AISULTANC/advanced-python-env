def inside(x, y, a, b, r):
    return (x - a)**2 + (y - b)**2 < r*r

a, b, r = map(float, input().split())
points = [tuple(map(float, input().split())) for _ in range(3)]

count = 0
for p in points:
    if inside(p[0], p[1], a, b, r):
        count += 1

print(count)
