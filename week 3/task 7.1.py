def rect_area(x, y):
    return x * y

def tri_area(a, b):
    return a * b / 2

x, y, z, t = map(float, input().split())

area = rect_area(x, y) + tri_area(z, t)
print(area)
