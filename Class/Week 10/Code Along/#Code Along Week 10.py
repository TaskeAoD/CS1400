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
        
    def accelerate(self, value):
        if not self.started:
            print("The car is not started.")
            return
        if self.speed + value <= self.max_speed:
            self.speed += value
        else:
            self.speed = self.max_speed 
        print(f"Accelerating to {self.speed} km/h....")
        
    def brake(self, value):
        if self.speed - value >= 0:
            self.speed -= value
        else:
            self.speed = 0  
        print(f"Braking to {self.speed} km/h....")  
    
    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.color}"    

    def __repr__(self):
        return(
            
            f"{type(self).__name__}"
            f'(make = "{self.make}", '
            f'model = "{self.model}", '
            f'year = "{self.year}", '
            f'color = "{self.color}")'
        )

def main():
    try:
        #create a bunch of vehicles with different models, colors, years, and makes
        car1 = Vehicle("Toyota", "Camry", 2024, "White")
        car2 = Vehicle("GMC", "Yukon XL", 2015, "Black")
        car3 = Vehicle("Kia", "Sorrento", 2019, "Blu")
        car4 = Vehicle("Honda", "CRV", 2025, "Orange")
        
        vehicles = [car1, car2, car3, car4]
        for vehicle in vehicles:
            print(vehicle)
        
    except ValueError as e:
        print(f"Error: {e}")
        
main()