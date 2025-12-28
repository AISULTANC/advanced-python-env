n = int(input())

for i in range(1, n + 1):
    ok = True
    for d in str(i):
        if d == '0' or i % int(d) != 0:
            ok = False
            break
    if ok:
        print(i, end=" ")
