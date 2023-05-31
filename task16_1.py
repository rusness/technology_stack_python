class CashRegister:
    def __init__(self, money):
        self.money = money
    
    def top_up(self, x):
        self.money += x
    
    def count_1000(self):
        return self.money // 1000
    
    def take_away(self, x):
        if self.money >= x:
            self.money -= x
        else:
            print("Not enough money in cash register")

a = CashRegister(100)

a.top_up(800)

print(a.money)

print(a.count_1000())

a.take_away(1000)
