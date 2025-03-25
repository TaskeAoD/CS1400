import time
import random

class Digital_Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50  # 0-100%, lower is better
        self.health = 100  # 0-100%, higher is better
        self.happiness = 50  # 0-100%, higher is better
        self.age = 0  # Pet's age in days
        self.alive = True

    def feed(self): #Option to feed
        if self.alive:
            self.hunger = max(0, self.hunger - 10)
            self.health = min(100, self.health + 5)
            print(f"{self.name} has been fed. Hunger: {self.hunger}, Health: {self.health}")
        else:
            print(f"{self.name} has passed away...")

    def walk(self): #Option to go on walk
        if self.alive:
            self.happiness = min(100, self.happiness + 10)
            self.hunger = min(100, self.hunger + 5)
            print(f"{self.name} went for a walk! Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} has passed away...")

    def pet(self): #Option to pet
        if self.alive:
            self.happiness = min(100, self.happiness + 5)
            print(f"{self.name} enjoyed some petting! Happiness: {self.happiness}")
        else:
            print(f"{self.name} has passed away...")

    def age_up(self): #Option to wait(ages the pet)
        if self.alive:
            self.age += 1
            self.hunger = min(100, self.hunger + 10)
            self.happiness = max(0, self.happiness - 5)
            self.health = max(0, self.health - 5)

            print(f"{self.name} is now {self.age} days old. Hunger: {self.hunger}, Happiness: {self.happiness}, Health: {self.health}")

            if self.hunger >= 100 or self.health <= 0 or self.happiness <= 0:
                self.alive = False
                print(f"Sadly, {self.name} has passed away...")
    
    def status(self): #Check status
        if self.alive:
            print(f"{self.name}'s Status - Hunger: {self.hunger}, Health: {self.health}, Happiness: {self.happiness}, Age: {self.age}")
        else:
            print(f"{self.name} has passed away...")
            

#Start Game Loop Here
pet_name = input("What is your Digital Pet's name? ")
pet = Digital_Pet(pet_name)

while pet.alive:
    action = input("Choose an action(feed, walk, pet, status, wait): ").strip().lower()
    if action == "feed":
        pet.feed()
    elif action == "walk":
        pet.walk()
    elif action == "pet":
        pet.pet()
    elif action == "status":
        pet.status()
    elif action == "wait":
        print("Time passes...")
        time.sleep(2)  # Simulating time passing
        pet.age_up()
    else:
        print("Action not valid. Please try again.")

print(f"Game over. Your Digital Pet, {pet_name} has passed away.")
