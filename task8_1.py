N = int(input("Введите количество элементов: "))

numbers = []
for i in range(N):
    number = int(input())
    numbers.append(number)

reversed_numbers = []
for i in range(N-1, -1, -1):
    reversed_numbers.append(numbers[i])

for number in reversed_numbers:
    print(number)
