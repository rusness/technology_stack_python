s = input("Введите строку: ")

result = ""
for i in range(len(s)):
    if s[i] != " " or (i > 0 and s[i-1] != " "):
        result += s[i]

print(result)
