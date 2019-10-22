num = list(map(int,input('Please Enter the numbers: ').split()))  # Multiple number Input
Missing_numbers = [x for x in range(2,21) if x not in num]  # Find missing number
print('missing numbers:', Missing_numbers)


