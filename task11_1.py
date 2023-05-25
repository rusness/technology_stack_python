def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_list(n):

    fact_list = []
    for i in range(n, 0, -1):
        fact_list.append(factorial(i))
    return fact_list

num = int(input("Введите натуральное число: "))
fact_num = factorial(num)
print("Факториал числа", num, "равен", fact_num)
fact_list = factorial_list(fact_num)
print("Список факториалов числа", fact_num, "в убывающем порядке:", fact_list)
