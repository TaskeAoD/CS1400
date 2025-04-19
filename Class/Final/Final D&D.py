import os

class Character: #Full Class for character creation info
    def __init__(self, name, player, race, character_class, strength, constitution, dexterity, intelligence, wisdom, charisma):
        self.name = name
        self.player = player
        self.character_class = character_class
        self.race = race
        self.attributes = {
            "Strength": strength,
            "Constitution": constitution,
            "Dexterity": dexterity,
            "Intelligence": intelligence,
            "Wisdom": wisdom,
            "Charisma": charisma
        }

    def display_character(self):  #Displays the final character details.
        print("\n-=-=-=Character Sheet=-=-=-")
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Class: {self.character_class}")
        print("Attributes:")
        for key, value in self.attributes.items():
            print(f"{key}: {value}")

class Game: #Class to handle character creation
   
    def __init__(self):
        self.character = None  # Placeholder for the created character

    def get_valid_input(self, prompt, options): #Ensures input is valid and matches what is displayed
        while True:  #Code taken and modified for this use from https://discuss.python.org/t/multi-purpose-function-for-simple-user-input/18046/2
            choice = input(prompt).strip().capitalize() #User: Vbrozik on the Python.org forums, Aug 2022
            if choice in options:  #Issues I ran into were that theirs called the question and mine needed the self tag
                return choice
            print("Invalid choice, please try again.")

    def create_character(self): #Character Creation Part

        print("Welcome to the simple D&D Character Creator!\nThis will be using a simplified 5e point allocation system!")

        name = input("Enter your character's name: ").strip().capitalize()
        player = input(f"Who is playing {name}: ").strip().capitalize()
        
        races = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"]
        race = self.get_valid_input(f"Choose a race {races}: ", races)

        classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
        character_class = self.get_valid_input(f"Choose a class {classes}: ", classes)

        print("\nNow, assign 27 points to your attributes (Strength, Constitution, Dexterity, Intelligence, Wisdom, Charisma.)")
        
        points = 27
        attributes = {"Strength": 8, "Constitution": 8, "Dexterity": 8, "Intelligence": 8, "Wisdom": 8, "Charisma": 8}

        for attr in attributes.keys():
            while True:
                try:
                    value = int(input(f"Assign points to {attr} (Remaining: {points}): "))
                    if 0 <= value <= points:
                        attributes[attr] = value + 8
                        points -= value
                        break
                    else:
                        print("Invalid amount. You must assign within the remaining points.")
                except ValueError:
                    print("Please enter a valid number.")
                    

        self.character = Character(name, player, race, character_class, 
                                   attributes["Strength"], attributes["Constitution"], attributes["Dexterity"], attributes["Intelligence"], attributes["Wisdom"], attributes["Charisma"])
        print("\nCharacter creation complete!") 
        
    def sheet(self): #Function to save to text file.
        save = input("\nWould you like to save this Character? (Y/N): ").strip().lower()
        if save == "y":
            filename = f"{self.character.name}_character.txt"
            with open(filename, "w") as file:
                file.write("-=-=-=Character Sheet=-=-=-\n")
                file.write(f"Character Name: {self.character.name}\n")
                file.write(f"Player Name: {self.character.player}\n")
                file.write(f"Class: {self.character.character_class}\n")
                file.write(f"Race: {self.character.race}\n")
                file.write(f"Attributes:\n")
                for key, value in self.character.attributes.items():
                    file.write(f"   {key}: {value}\n")
                print(f"\nCharacter saved to '{self.character.name}.txt'!")        
        else:
            print("Character not saved.") 
     
    def play(self): #Actual part, running the functions from the class
        self.create_character()
        self.character.display_character()
        self.sheet()
        

if __name__ == "__main__": #Call to run the system
    game = Game()
    game.play()
