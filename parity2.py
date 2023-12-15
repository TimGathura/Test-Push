def main():
    x = int(input('Put in a number boi! '))

    if is_even(x):
        print(f'{x} is an EVEN number boi!')
    else:
        print(f'{x} is an ODD number boi!')


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()