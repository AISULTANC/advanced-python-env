s1 = input()
s2 = input()

if len(s1) != len(s2):
    print("NO")
else:
    count1 = {}
    count2 = {}
    
    for char in s1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1

    for char in s2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1

    if count1 == count2:
        print("YES")
    else:
        print("NO")