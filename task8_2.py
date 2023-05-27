n = int(input("Введиче кол-вл чсиле N:"))
arr = list(map(int, input("Введите числа через пробел: ").split()))

temp = arr[-1]

for i in range(n-2, -1, -1):
    arr[i+1] = arr[i]

arr[0] = temp

print(*arr)
