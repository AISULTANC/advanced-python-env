import math

def triangle_area(a):
    return (math.sqrt(3) / 4) * a * a

a = float(input())
hex_area = 6 * triangle_area(a)
print(hex_area)
