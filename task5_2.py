word = input("Введите слово: ")
# гласные буквы a, e, i , o, u
sum_a = 0
sum_e = 0
sum_i = 0
sum_o = 0
sum_u = 0

for i in word:
    letter = i.lower()
    if letter == 'a':
        sum_a += 1
    elif letter == 'e':
        sum_e += 1
    elif letter == 'i':
        sum_i += 1
    elif letter == 'o':
        sum_o += 1
    elif letter == 'u':
        sum_u += 1
if sum_a > 0:
    print("Количество 'a' -", sum_a)
else:
    print("Количество 'a' -", sum_a>0)

if sum_e > 0:
    print("Количество 'e' -", sum_e)
else:
    print("Количество 'e' -", sum_e>0)

if sum_i > 0:
    print("Количество 'i' -", sum_i)
else:
    print("Количество 'i' -", sum_i>0)

if sum_o > 0:
    print("Количество 'o' -", sum_o)
else:
    print("Количество 'o' -", sum_o>0)

if sum_u > 0:
    print("Количество 'u' -", sum_u)
else:
    print("Количество 'u' -", sum_u>0)