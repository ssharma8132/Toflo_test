Number_1 = int(input('Enter First Number:'))  # First input
Number_2 = int(input('Enter second Number:'))  # second input

while Number_2 != 0:
    (Number_1, Number_2) = (Number_2, Number_1 % Number_2)  # division logic
print('Greatest common division is:', Number_1)  # printing best division

