def swap(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

m = int(input())
arr = list(map(int, input().split()))

print(arr)
swap(arr)
print(arr)
