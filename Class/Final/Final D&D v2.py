import os

# Dictionary containing racial bonuses based on D&D 5e rules
RACE_BONUSES = {
    "Dwarf": {"Constitution": 2},
    "Elf": {"Dexterity": 2},
    "Halfling": {"Dexterity": 2},
    "Human": {"Strength": 1, "Constitution": 1, "Dexterity": 1, "Intelligence": 1, "Wisdom": 1, "Charisma": 1},
    "Dragonborn": {"Strength": 2, "Charisma": 1},
    "Gnome": {"Intelligence": 2},
    "Half-Elf": {"Charisma": 2, "Choice": 2},  # Two ability scores of choice get +1
    "Half-Orc": {"Strength": 2, "Constitution": 1},
    "Tiefling": {"Charisma": 2, "Intelligence": 1}
}

# Dictionary containing class bonuses (optional, since most classes don't modify attributes directly)
CLASS_BONUSES = {
    "Barbarian": {"Strength": 1},
    "Bard": {"Charisma": 1},
    "Cleric": {"Wisdom": 1},
    "Druid": {"Wisdom": 1},
    "Fighter": {"Strength": 1},
    "Monk": {"Dexterity": 1},
    "Paladin": {"Strength": 1, "Charisma": 1},
    "Ranger": {"Dexterity": 1},
    "Rogue": {"Dexterity": 1},
    "Sorcerer": {"Charisma": 1},
    "Warlock": {"Charisma": 1},
    "Wizard": {"Intelligence": 1}
}

class Character:
    def __init__(self, name, player, race, character_class, attributes):
        self.name = name
        self.player = player
        self.character_class = character_class
        self.race = race
        self.attributes = attributes
        self.apply_racial_bonuses()
        self.apply_class_bonuses()

    def apply_racial_bonuses(self):
        """Apply racial bonuses to attributes."""
        if self.race in RACE_BONUSES:
            for attr, bonus in RACE_BONUSES[self.race].items():
                if attr == "Choice":  # Handle Half-Elf flexible bonus
                    for _ in range(2):  # Half-Elf chooses two attributes to get +1
                        print(f"Half-Elf bonus! Choose an attribute to increase: {list(self.attributes.keys())}")
                        choice = input("Enter attribute: ").strip().capitalize()
                        while choice not in self.attributes:
                            print("Invalid choice. Try again.")
                            choice = input("Enter attribute: ").strip().capitalize()
                        self.attributes[choice] += 1
                else:
                    self.attributes[attr] += bonus

    def apply_class_bonuses(self):
        """Apply class bonuses to attributes (if applicable)."""
        if self.character_class in CLASS_BONUSES:
            for attr, bonus in CLASS_BONUSES[self.character_class].items():
                self.attributes[attr] += bonus

    def display_character(self):
        """Display character details."""
        print("\n===== Character Sheet =====")
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Class: {self.character_class}")
        print("Attributes:")
        for key, value in self.attributes.items():
            print(f"{key}: {value}")

class Game:
    def __init__(self):
        self.character = None

    def get_valid_input(self, prompt, options):
        """Ensures input is valid and matches displayed options."""
        while True:
            choice = input(prompt).strip().capitalize()
            if choice in options:
                return choice
            print("Invalid choice, please try again.")

    def create_character(self):
        """Handles character creation, including assigning attributes and applying bonuses."""
        print("Welcome to the simple D&D Character Creator!")
        print("This will be using a simplified 5e point allocation system!")

        name = input("Enter your character's name: ").strip().capitalize()
        player = input(f"Who is playing {name}: ").strip().capitalize()

        races = list(RACE_BONUSES.keys())
        race = self.get_valid_input(f"Choose a race {races}: ", races)

        classes = list(CLASS_BONUSES.keys())
        character_class = self.get_valid_input(f"Choose a class {classes}: ", classes)

        print("\nNow, assign 27 points to your attributes (Base starts at 8 for each).")

        points = 27
        attributes = {"Strength": 8, "Constitution": 8, "Dexterity": 8, "Intelligence": 8, "Wisdom": 8, "Charisma": 8}

        for attr in attributes.keys():
            while True:
                try:
                    value = int(input(f"Assign points to {attr} (Remaining: {points}): "))
                    if 0 <= value <= points:
                        attributes[attr] += value
                        points -= value
                        break
                    else:
                        print("Invalid amount. You must assign within the remaining points.")
                except ValueError:
                    print("Please enter a valid number.")

        self.character = Character(name, player, race, character_class, attributes)
        print("\nCharacter creation complete!")

    def sheet(self):
        """Save character sheet to a file."""
        save = input("\nWould you like to save this Character? (Y/N): ").strip().lower()
        if save == "y":
            filename = f"{self.character.name}_character.txt"
            with open(filename, "w") as file:
                file.write("-=-=-=Character Sheet=-=-=-\n")
                file.write(f"Character Name: {self.character.name}\n")
                file.write(f"Player Name: {self.character.player}\n")
                file.write(f"Class: {self.character.character_class}\n")
                file.write(f"Race: {self.character.race}\n")
                file.write("Attributes:\n")
                for key, value in self.character.attributes.items():
                    file.write(f"   {key}: {value}\n")
                print(f"\nCharacter saved to '{filename}'!")        
        else:
            print("Character not saved.") 

    def play(self):
        """Run the character creation process."""
        self.create_character()
        self.character.display_character()
        self.sheet()

if __name__ == "__main__":
    game = Game()
    game.play()
