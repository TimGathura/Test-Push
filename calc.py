#Ask user for input of two numbers
#Add the two numbers 
#Multiply the two numbers
#Display the output on the screen; both addition and multiplication
#Format output to our liking

num1 = input('Enter the first number: ')
print()

num2 = float(input('Enter the second number: '))
print()

sum = float(num1) + num2
sum = round(sum, 3)

mult = float(num1) * num2
mult = round(mult, 3)

mod = float(num1) % num2
mod = round(mod)

print(f'The sum of the {num1} and {num2} is {sum}.')
print(f'The multiplication of {num1} and {num2} is {mult}.')
print(f'The remainder after division of {num1} by {num2} is {mod}')

x = num1, num2
print(x)
