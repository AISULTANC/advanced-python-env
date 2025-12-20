lst = input().split()

max_len = 0
for s in lst:
    if len(s) > max_len:
        max_len = len(s)

for i in range(len(lst)):
    if len(lst[i]) < max_len:
        lst[i] = lst[i] + "_" * (max_len - len(lst[i]))

print(lst)
