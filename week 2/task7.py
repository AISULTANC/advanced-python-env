items = input().split()

count = {}
for x in items:
    count[x] = count.get(x, 0) + 1

print("Purchase frequency:")
for k in count:
    print(k + ":", count[k])

popular = max(count, key=count.get)
print("\nMost popular item:", popular)

print("\nPurchased once:")
for k in count:
    if count[k] == 1:
        print(k, end=" ")

print("\n\nSorted by frequency:")
for k, v in sorted(count.items(), key=lambda x: -x[1]):
    print(k, v)
