#Code Along ADHD
#Non-ADHD range = 10+
#ADHD = 1-9
#Organize time effectively: 3 points
#Timely homework: 5 points
#Manage sequential tasks: 3 points
#Keeps room organized: 1 point
#Attention to detail: 1 point

score = 0

print("This is a test to determine characteristics of ADHD, but is not a diagnostic tool.")
print("You will need to score your child in various categories from low to high or yes or no")

organize = int(input("How well does your child organize things (1-3)? "))
if organize > 3:
    print("Score entered to high for test, will give inaccurate result.")
elif organize > 1:
    print("Score entered to low for test, will give inaccurate result.")
else: print(f"The score you entered was {organize}")
score += organize

homework = int(input("How timely does your child do homework and turn it in (1-5)? "))
if homework > 5:
    print("Score entered to high for test, will give inaccurate result.")
elif homework > 1:
    print("Score entered to low for test, will give inaccurate result.")
else: print(f"The score you entered was {homework}")
score += homework

tasks = int(input("How well does your child do with tasks in order (1-3)? "))
if tasks > 3:
    print("Score entered to high for test, will give inaccurate result.")
elif tasks > 1:
    print("Score entered to low for test, will give inaccurate result.")
else: print(f"The score you entered was {tasks}")
score += tasks

room = int(input("Is your child's room organized? (1 = yes, 0 = no)? "))
if room > 1:
    print("Score entered to high for test, will give inaccurate result.")
elif room > 0:
    print("Score entered to low for test, will give inaccurate result.")
else: print(f"The score you entered was {room}")
score += room

detail = int(input("Does your child pay attention to detail? (1 = yes, 0 = no) "))
if detail > 1:
    print("Score entered to high for test, will give inaccurate result.")
elif detail > 0:
    print("Score entered to low for test, will give inaccurate result.")
else: print(f"The score you entered was {detail}")
score += detail

score = organize + homework + tasks + room + detail

print(f"Final score is {score}")
if score >= 14: print("Score is above permitted range, assessment is inaccurate.")
elif score >= 10: print("Your child may not have ADHD")
else: print("Your child may have ADHD")