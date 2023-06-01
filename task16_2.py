class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s
    
    def go_down(self):
        self.y -= self.s
    
    def go_left(self):
        self.x -= self.s
    
    def go_right(self):
        self.x += self.s
    
    def evolve(self):
        self.s += 1
    
    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            print("Cannot degrade S below 1 !!!")
    
    def count_moves(self, x2, y2):
        x_diff = abs(x2 - self.x)
        y_diff = abs(y2 - self.y)
        if x_diff % self.s == 0 and y_diff % self.s == 0:
            total_moves = (x_diff // self.s) + (y_diff // self.s)
        else:
            total_moves = 0
        return total_moves

a = Turtle(0,0,1)
a.go_up()
a.go_up()
a.evolve()
print(a.y, a.x)

print(a.count_moves(5,5))
