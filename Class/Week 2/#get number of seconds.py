#get number of seconds
seconds = int(input("Please enter the number of seconds: "))
#days
days = seconds // 86400
seconds = seconds % 86400
#first compute number of hours in the given number of seconds
hours = seconds // 3600
#Compute the remaining seconds after the hours are accounted for
seconds = seconds % 3600
#next compute the number of minutes in the remaining number of seconds
minutes = seconds // 60
#compute the remaining seconds after minutes are accounted for
seconds = seconds % 60
#report results
print(hours, ":", sep= "", end="")
#compute the tens digit of minutes
tens = minutes // 10
#compute the one digit of minutes
ones = minutes % 10
print(tens, ones, ":", sep="", end="")
#compute tens digits of seconds
tens = seconds // 10
#compute ones digits of seconds
ones = seconds % 10
print(tens, ones, sep="")