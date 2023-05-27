n = int(input("Введите число N: "))
arr = list(map(int, input("Введите числа через пробел: ").split()))

unique_elements = set(arr)
print(len(unique_elements))
