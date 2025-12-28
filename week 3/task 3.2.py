text = input().split()

result = []
for word in text:
    result.append("".join(sorted(word)))

print(" ".join(result))
