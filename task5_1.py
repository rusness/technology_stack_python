a = int(input("Введите число: "))

if a%2 == 0 and a > 0:
    print("положительное четное число")
elif a%2 == 0 and a < 0:
    print("отрицательное четное число")
elif a%2 != 0:
    print("число не является четным")
elif a==0:
    print("нулевое число")