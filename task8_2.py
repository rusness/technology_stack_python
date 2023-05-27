n = int(input())
arr = list(map(int, input().split()))

temp = arr[-1]

for i in range(n-2, -1, -1):
    arr[i+1] = arr[i]

arr[0] = temp

print(*arr)
