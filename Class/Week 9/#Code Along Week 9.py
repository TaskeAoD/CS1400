#Code Along Week 9, l# = Line number comment is attached to due to tab lining and as a countermeasure to copying
'''Shopping list
Add Items, Remove Items, View List
Read, write, open, close files'''
list = [] #Array for the shopping list
file = "Groceries.txt"
#Load/Create file into the list
def LoadList():
    print(f"Loading {file}")
    
    try:
        f = open(f"{file}", 'r')                #Opening file in 'read' mode l12
        for line in f:
            line = line.strip()
            list.append(line)
        f.close()                               #This will close the file l16
    except FileNotFoundError as err:
        print(err)
        print(f"Creating {file}")
        f = open(f"{file}", 'w')                #This will create the file if it doesn't exist already l20
        f.close()

def AddItem():
    item = input("What Item do you want to add to the list? ")
    list.append(item)                           #Appends list with item l25
    
    try:
        print(f"Adding {item} to {file}")
        f =  open(f"{file}", 'a')               #Opens Groceries.txt to append the item to the list l28
        f.write(item + "\n")                    #Adds item to list, the creates new line l29
        f.close()                               #Closes file l30
        
    except FileNotFoundError as err:
        print(err)
        
def ViewList():
    print(f"Here are the items in your {file} list:")
    for i in list:                              #Iterates list through each item l38
        print(i)                                #Prints each item found in list l39
        
def SaveList():
    try:
        f = open(file, 'w')
        for i in list:                          #For each item in the list write to file l44
            f.write(i + "\n")                   #Write each item into the file on a new line l45
        f.close()                               #Close the file after all items are added to the file l46
        
    except FileNotFoundError as err:
        print(err)
        
def RemoveItems():
    try:
        item = input(f"What item would you like to remove from {file}? ")
        list.remove(item)                       #Removes Item from list l54
        ViewList()
        SaveList()
        
    except ValueError as err:
        print(f"{item} is not found on {file}. Items are Case-Sensitive.")
        ViewList()
        
    
def Menu():
    
    

LoadList()
AddItem()
ViewList()
#SaveList()
RemoveItems()
