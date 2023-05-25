pets = {}
petinfo={}

nameofpet = input("Введите имя питомца: ")

kindofpet = input("Вид питомца: ")
ageofpet  = int(input("Возраст питомца: "))
nameofowner = input("Имя владельца: ")

petinfo["Вид питомца"] = kindofpet
petinfo["Возраст питомца"] = ageofpet
petinfo["Имя владельца"] = nameofowner

pets[nameofpet] = petinfo


for pet in pets:

    print("Это ", pets[pet]["Вид питомца"], " по кличке: ", pet, ". Возраст питомца: ", pets[pet]["Возраст питомца"], end = " ")
    print("год" if pets[pet]["Возраст питомца"] % 10 == 1 and pets[pet]["Возраст питомца"] != 11 else ("года" if pets[pet]["Возраст питомца"] % 10 in [2, 3, 4] and not (pets[pet]["Возраст питомца"] % 100 in [12, 13, 14]) else "лет"), end=". ")
    print("Имя владельца:", pets[pet]["Имя владельца"], end=".")

