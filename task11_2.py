import collections

pets = {}

def get_pet(id):

    if id in pets:
        return pets[id]

    return False

def create():

    key = 0
    if 1 in pets:
        key = collections.deque(pets, maxlen=1)[0]

    key+=1


    # добавляем запись
    petname = {}
    pet = {}
    name = input("Имя питомца: ")
    kind = input("Вид питомца: ")
    age  = int(input("Возраст питомца: "))
    owner = input("Владелец: ")


    pet["Вид питомца"] = kind
    pet["Возраст питомца"] = age
    pet["Владелец"] = owner

    petname[name] = pet
    pets[key] = petname



def get_suffix(age):
    if age % 10 == 1 and age != 11:
        return "год"
    elif age % 10 in [2, 3, 4] and not (age % 100 in [12, 13, 14]):
        return  "года"
    else:
        return "лет"

def read(id):


    pet = get_pet(id)

    if pet == False:
        print("Питомца с таким ID не существует")
    else:
        for name in pet:
            suffixage = get_suffix(pet[name]["Возраст питомца"])
            print(f"Это {pet[name]['Вид питомца']} по кличке: {name}. Возраст питомца {pet[name]['Возраст питомца']} {suffixage}.", end = " ")
            print(f"Имя владельца: {pet[name]['Владелец']}.")



def update(id):

    pet = get_pet(id)
    if pet == False:
        print("Питомца с таким ID не существует")
    else:
        # запрашивамеи информацию
        for name in pet:
            print(f"Изменение информации по питомцу {name}")
            print("\n")

            kind = input("Вид питомца: ")
            age  = int(input("Возраст питомца: "))
            owner= input("Владелец: ")

            if not kind == "":
                pet[name]["Вид питомца"] = kind

            if not age == 0:
                pet[name]["Возраст питомца"] = age

            if not owner == "":
                pet[name]["Владелец"] = owner

def delete(id):

    pet = get_pet(id)
    if pet == False:
        print("Питомца с таким ID не существует")
    else:
        del pets[id]

def pet_list():

    for key in pets:

        pet_name = pets[key]
        print(f"id - {key}; {pet_name}")
    if len(pets) == 0:
        print("Список пуст.")


while True:
    command = input("Введите команду (stop- для выхода): ").lower()
    if command=="stop":
        print("Программа завершена!")
        break
    elif command == "create":
        create()
    elif command == "read":
        id = int(input("Введите id: "))
        read(id)
    elif command == "update":
        id = int(input("Введите id: "))
        update(id)
    elif command ==  "petlist":
        pet_list()
    elif command == "delete":
        id = int(input("Введите id: "))
        delete(id)

