#To check whether a number is even or odd

#Accept user input
x = int(input('Enter x: '))

#parity check
if x % 2  == 0:
    print(f'{x} is even')
else:
    print(f'{x} is odd')

y = int(input('Enter y: '))

if y % 8 == 0:
    print(f'{y} is divisible by 8')
else: 
    print(f'{y} is NOT divisible by 8')
