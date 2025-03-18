one = 1.0
one_third = 1.0/3.0
one_fourth = 1.0/4.0
one_tenth = 1.0/10.0
zero = one - one_third - one_third - one_third
zero3 = one - one_fourth - one_fourth - one_fourth - one_fourth
zero2 = one - one_tenth - one_tenth - one_tenth - one_tenth - one_tenth - one_tenth - one_tenth - one_tenth - one_tenth - one_tenth
print(f'one = {one}. one_third = {one_third}, zero = {zero}')
print(f'one = {one}. one_tenth = {one_tenth}, zero = {zero2}')
print(f'one = {one}. one_fourth = {one_fourth}, zero = {zero3}')

x = 4
y = 10.2
z = 5
sum = x + y * z
print(sum)