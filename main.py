#Use main function, and two user defined functions
#The functions should also use methods of choice to add nuances.
#Ask for 3 details from the user.
#Print out info with minimal text using the functions.

def main():
    fullname = input('What is your name? ')
    fullname = fullname.strip().title()
    fname, lname = fullname.split(' ')

    sal = int(input(f'Thank you {fname}. Please input your salary: '))
    print()

    gender = input('Great, input your gender: ')
    gender = gender.strip().lower()
    print()

    A(fname, lname, sal, gender)



def A(x,y,z='1000000',a='female'):

    print('Please confirm that this is the correct info: ')
    print(f'First Name: {x}')
    print(f'Last Name: {y}')
    print(f'Salary: {z:,}')
    print(f'Gender: {a}')
    print()


main()   