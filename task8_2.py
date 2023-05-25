N = int(input("Введите число N: "))

numbers = []
for i in range(N):
    number = int(input())
    numbers.append(number)

for i in range(N//2):
    numbers[i], numbers[N-i-1] = numbers[N-i-1], numbers[i]

for number in numbers:
    print(number)
