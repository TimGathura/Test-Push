#create functions that convert the input from str to float
#Remove $ from the input and convert the rest of input to float
#Remove % from the input and convert the rest of input to float
#Print result of new functions as needed

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #code
    d = d.replace('$', '')
    d = float(d)
    return float(d)


def percent_to_float(p):
    # TODO
    p = p.replace('%','')
    p = float(p)
    p = p / 100
    return float(p)

main()
