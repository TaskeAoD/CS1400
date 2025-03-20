#Code Along Week 10

class Vehicle:
    
    def __init__(self, make, model, year, color): #init needs to start with 'self' no matter what
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200
        

ford_mustang = Vehicle("Ford", "Mustang", 1967, "Black")

print(ford_mustang.color)
print(ford_mustang.year)
print(ford_mustang.model)
print(ford_mustang.make)