n = input("Введите числа через пробел: ")
numbers = n.split()
seen = set()
for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)
