import os

class Character:
    """Class to create a D&D character with attributes."""
    def __init__(self, name, player, character_class, race, strength, dexterity, agility, intelligence, wisdom, charisma):
        self.name = name
        self.player = player
        self.character_class = character_class
        self.race = race
        self.attributes = {
            "Strength": strength,
            "Dexterity": dexterity,
            "Agility": agility,
            "Intelligence": intelligence,
            "Wisdom": wisdom,
            "Charisma": charisma
        }

    def display_character(self): #At the end this will display the sheet
        print("\n===== Character Sheet =====")
        print(f"Name: {self.name}")
        print(f"Class: {self.character_class}")
        print(f"Race: {self.race}")
        print("Attributes:")
        for key, value in self.attributes.items():
            print(f"  {key}: {value}")
            
    def sheet(self): #Function required to save character sheet
        filename = f"{self.name}_character.txt"
        with open(filename, "w") as file:
            file.write("-=-=-=Character Sheet=-=-=-\n")
            file.write(f"Character Name: {self.name}\n")
            file.write(f"Player Name: {self.player}\n")
            file.write(f"Class: {self.character_class}\n")
            file.write(f"Race: {self.race}\n")
            file.write(f"Attributes:\n")
            for key, value in self.attributes.items():
                file.write(f"   {key}: {value}\n")
        print("\nCharacter saved to '{filename}'!")


class Game: #Class for all of the creator functions
    def __init__(self):
        self.character = None  # Placeholder for the created character

    def getInput(self, prompt, options):
        """Ensures valid input from a list of options."""
        while True:
            choice = input(prompt).strip().capitalize()
            if choice in options:
                return choice
            print("Invalid choice, please try again.")

    def create_character(self): #Character Creator it self
        print("Welcome to a basic D&D Character Creator!\nThis will be using the 5e point buy system!")
        #print("Make sure when you add the points to your character sheet you include the base 8 you start out with.") #This is here because I couldn't get the base 8 to work for a while
        
        name = input("Enter your character's name: ")
        player = input(f"Who is playing {name}: ")

        classes = ["Fighter", "Sorcerer", "Rogue", "Artificer"]
        character_class = self.getInput(f"Choose a class {classes}: ", classes)

        races = ["Human", "Elf", "Dwarf", "Orc"]
        race = self.getInput(f"Choose a race {races}: ", races)  #test

        print("\nNow, assign 27 points to your attributes (Strength, Dexterity, Agility, Intelligence, Wisdom, Charisma).")
        
        points = 27
        attributes = {"Strength": 8, "Dexterity": 8, "Agility": 8, "Intelligence": 8, "Wisdom": 8, "Charisma": 8} #In Point Buy each attribute starts out at 8

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
                    
        if self.race == "Elf":
            attributes
        elif:
            

        self.character = Character(name, player, character_class, race, 
                                   attributes["Strength"], attributes["Dexterity"], attributes["Agility"], attributes["Intelligence"], attributes["Wisdom"], attributes["Charisma"])
        print("\nCharacter creation complete!")

    def play(self):
        """Starts the character creation process and displays the character."""
        self.create_character()
        self.character.display_character()
        
        '''save = input("\nWould you like to save this Character? (Y/N): ").strip().lower()
        if save == "y":
            self.sheet()
        else:
            print("Character not saved.")'''


# Run the game
if __name__ == "__main__":
    game = Game()
    game.play()
