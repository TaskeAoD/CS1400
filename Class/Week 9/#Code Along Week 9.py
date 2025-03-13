#Code Along Week 9
'''Shopping list
Add Items, Remove Items, View List
Read, write, open, close files'''
list = [] #Array for the shopping list
file = "Groceries.txt"
#Load/Create file into the list
def LoadList():
    print(f"Loading {file}")
    
    try:
        f = open(f"{file}", 'r')                #Opening file in 'read' mode
        for line in f:
            line = line.strip()
            list.append(line)
        f.close()                               #This will close the file
    except FileNotFoundError as err:
        print(err)
        print(f"Creating {file}")
        f = open(f"{file}", 'w')                #This will create the file if it doesn't exist already
        f.close()

def AddItem():
    item = input("What Item do you want to add to the list? ")
    list.append(item)                           #Appends list with item
    
    try:
        print(f"Adding {item} to {file}")
        '''f =  open(f"{file}", 'a')               #Opens Groceries.txt to append the item to the list
        f.write(item + "\n")                    #Adds item to list, the creates new line
        f.close()'''                               #Closes file
        SaveList()
    except FileNotFoundError as err:
        print(err)
        
def ViewList():
    print(f"Here are the items in your {file} list:")
    for i in list:                              #Iterates list through each item
        print(i)                                #Prints each item found in list
        SaveList()
        
def SaveList():
    try:
        f = open(file, 'w')
        for i in list:                          #For each item in the list write to file
            f.write(i + "\n")                   #Write each item into the file on a new line
        f.close()                               #Close the file after all items are added to the file
        
    except FileNotFoundError as err:
        print(err)
        
def RemoveItems():
    try:
        item = input(f"What item would you like to remove from {file}? ")
        list.remove(item)                       #Removes Item from list l55
        ViewList()
        SaveList()
        
    except ValueError as err:
        print(f"{item} is not found on {file}. Items are Case-Sensitive.")
        ViewList()
        
    
def Menu():
    print(f"1: Add item to {file}")
    print(f"2: Remove item from {file}")
    print(f"3: Show items in {file}")
    print("4: Quit program")


choice = 0    
while choice != 4:
    ViewList()
    Menu()
    try:
        choice = int(input("Make a choice from the above options: "))
        if choice == 1:
            AddItem()
        if choice == 2:
            RemoveItems()
        if choice == 3:
            ViewList()
        if choice == 4:
            print("Thank you for using the List Generator!")
            break
        else:
            raise Exception ("Not a valid number.")
    except ValueError as err:
        print("Please enter an integer between 1 - 4")
    except:
        print("Please enter an integer between 1 - 4")
