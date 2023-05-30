class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def __str__(self):
        return f"Название автомобиля:{self.name} Скорость:{self.max_speed} Пробег:{self.mileage}"

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

class Autobus(Transport):
    def seating_capacity(self, capacity= 50):
        return super().seating_capacity(capacity)


a = Autobus("Рено", 120, 10000)
print(a)

print(a.seating_capacity())

    
    
