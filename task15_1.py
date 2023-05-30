class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def __str__(self):
        return f"Название автомобиля:{self.name} Скорость:{self.max_speed} Пробег:{self.mileage}"

class Autobus(Transport):
    pass


a = Autobus("Рено", 120, 10000)
print(a)


    
    
