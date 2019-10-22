num = int(input('Enter any number : '))  # input number
print('Input: ', num)  # print input value


a = (num // 100) % 10
b = (num // 10) % 10
c = (num // 1) % 10

j = [a,b,c]  # convert to list
j.sort(reverse=False)  # sort the list

if num < 99 or num > 999:  # check input is correct or not
    print("Please provide numbers between (100 to 999) only")
# separate the Digit from number
elif j[1] - j[0] < j[2] - j[1]:  # finding minimum difference
    remain = j[1] - j[0]
    print('Minimum number:',remain)
    new_index_value = (j[0]+remain)
    j[0] = new_index_value
    j[1],j[2] = j[2],j[1]
    print('Palindrome:',*j, sep="")

else:
    final_remain = j[2]-j[1]
    print('Minimum number:',final_remain)
    update_index_value = (j[1]+final_remain)
    j[1] = update_index_value
    j[1],j[0] = j[0],j[1]
    print('Palindrome: ',*j, sep="")


