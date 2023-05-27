
arr1 = set(map(int, input("Введите в список 1 числа через пробел: ").split()))
arr2 = set(map(int, input("Введите в список 2 числа через пробел: ").split()))

common_elements = arr1.intersection(arr2)
print(len(common_elements))
