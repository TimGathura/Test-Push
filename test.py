#Simple program to ask for users  details and display them on the screen
#Number of details: 6
#Details: First Name, Surname, Email Address, Sex, Town, DOB
#Issues: Lack of data type validation. How to change caps of a variable.

name = input('Please input your two names: ')
name = name.strip()
name = name.title()
first, last = name.split()

print()

EAddress = input('Please input your Email Address: ')
EAddress = EAddress.strip().lower()
print()

sex = input('Please input your Sex: ')
sex = sex.lower().strip()
print()

town = input('Please input your Town: ')
town = town.strip().capitalize()
print()

DOB = input('Please input your DOB: ')
DOB = DOB.strip()
print()

#Display
print('\'FINAL RESULT\'')
print("Subject's name: " + first, last)
print(f"{first}, can be contacted on {EAddress}. ", end='')
print(last, "'s gender is ", sex, ' and they live in ', town, '. ', sep='', end='')
print(first, " was born on ", DOB, '.', sep='')
