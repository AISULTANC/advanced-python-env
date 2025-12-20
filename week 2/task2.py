a = input()
b = input()

res = 0
n = len(b)

shifts = []
for i in range(n):
    shifts.append(b[i:] + b[:i])

for i in range(len(a) - n + 1):
    sub = a[i:i+n]
    if sub in shifts:
        res += 1

print(res)
