#Week 8 Day 2 Code Along
#Employee Time Card

#Employees need to enter work hours
#Work hours must be an integer
#Work hours must be between 0 and 80 hours for two week period
#Employees must enter name
#Print out the name from employee and their hours worked

#variable list
employeename = ''
hoursworked = ''
employeename = input('Please enter Employee name: ')
hoursworked = (input('Please enter hours worked (Between 0-80): '))

#function List
def checkPositiveNumberValue(hours):
    while True:
        try:
            hours = int(hours)
            if hours < 0 or hours > 80:
                raise IndexError("Invalid number of hours entered.  Hours worked must be between 0 and 80.")
            
            return hours
        except ValueError:
            print("Invalid number of hours entered in correct format.")
            hours = input('Please enter hours worked (Between 0-80): ')    
            return hours
        except:
            print("Value must be input in number format.")
            hours = input('Please enter hours worked (Between 0-80): ')


hoursworked = checkPositiveNumberValue(hoursworked)
#print(f'Employee: {employeename} has worked {hoursworked} hours during this pay period')
print("Employee: " + employeename + " worked " + str(hoursworked) + " hours during the time period.")