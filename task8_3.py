m = int(input("Вес лодки: "))
n = int(input("Количество рыбаков: "))

weights = []
for i in range(n):
    weight = int(input("Вес рыбака "+str(i+1)+ ": "))
    weights.append(weight)

weights.sort()  # сортируем рыбаков по возрастанию веса

boats = 0
while len(weights) > 0:
    heaviest = weights.pop()  # достаем самого тяжелого рыбака
    if len(weights) > 0 and heaviest + weights[0] <= m:
        lightest = weights.pop(0)  # достаем самого легкого рыбака
    else:
        lightest = heaviest
    boats += 1

print(boats)
