import math

shape = input("Enter shape (circle, rectangle, triangle): ")

if shape == "circle":
    r = float(input())
    area = math.pi * r * r
elif shape == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif shape == "triangle":
    h = float(input())
    b = float(input())
    area = 0.5 * h * b
else:
    area = 0

print(area)
