valid_letters = set("ABCEHKMOPTXY")

n = int(input())
for _ in range(n):
    plate = input()

    ok = True
    if len(plate) != 6:
        ok = False
    else:
        if plate[0] not in valid_letters:
            ok = False
        if not plate[1:4].isdigit():
            ok = False
        if plate[4] not in valid_letters or plate[5] not in valid_letters:
            ok = False

    if ok:
        print("Yes")
    else:
        print("No")
