class race:
    def __init__(self):
        pass
    
    def RaceList(self):
        race = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']
        #Dwarf: Con + 2
        if race == "Dwarf":
            {"Constitution": +2}
        #Elf: Dex + 2
        if race == "Elf":
            {"Dexterity": +2}
        #Halfling: Dex + 2
        if race == "Halfling":
            {"Dexterity": +2}
        #Human: All + 1
        if race == "Human":
            {"Strength": +1, "Constitution": +1, "Dexterity": +1, "Intelligence": +1, "Wisdom": +1, "Charisma": +1}
        #Dragonborn: Str + 2 Cha + 1
        if race == "Dragonborn":
            {"Strength": +2, "Charisma": +1}
        #Gnome: Int + 2
        if race == "Gnome":
            {"Intelligence": +2}
        #Half-Elf: Cha + 2 Rest + 1
        if race == "Half-Elf":
            {"Strength": +1, "Constitution": +1, "Dexterity": +1, "Intelligence": +1, "Wisdom": +1, "Charisma": +2}
        #Half-Orc: Str + 2 Con + 1
        if race == "Half-Orc":
            {"Strength": +2, "Constitution": +1}
        #Tiefling: Cha + 2 Int + 1
        if race == "Tiefling":
            {"Intelligence": +1, "Charisma": +1}
