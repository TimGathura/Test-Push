#Create a program to calculate the throughput of a machine in a week given the hours worked in a day
#Step1: Introduce the program to user.
#Step2: Ask for input of the number of hours worked per day.
#Step3: Calculation algorithm
#Step3: Display the possible range of throughput of the machine/ Exact throughput (-)

#Assumption1: Machine works 7 days a week with equal hours each day
#Assumption2: The capacity/rate of the machine production is constant
#Assumption3: 

#Nuance1: Ability of program to accept either total hours worked in a week or hours worked per day.
#Nuance2: Validate or only accept integers as input
#Nuance3: Ability to calculate throughput of various machines as needed.

#Lessons: Use of 'global' statement to make variables available in all namespaces.


#Step1
def main():
    print('         🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐      ')
    print('Hello there😀. I am a program designed to help you calculate the throughput of production machines.', end='\n\n')

#Step2
    #cap_day = throughput_day(input('How many hours will the machine be running in a day: '))
    #cap_week = throughput_week(input('How many days will the machine run during the week: '))
    hours = input('How many hours will the machine be running per day? ')
    days = input('How many days will the machine run in a week? ')
    print()

    product = 'caps'.capitalize()

    cap_day = throughput_day(hours)
    cap_day = int(cap_day)
    cap_week = throughput_week(days)
    cap_week = int(cap_week)

    print(f'Capacity per day: {cap_day:,}')
    print(f'Capacity per week: {cap_week:,}')
    print(f'📈 IMPLICATION 📈: ')
    print(f'If the machine runs for {days} hours a day, it can produce {cap_day:,} number of {product} in a day and {cap_week:,} {product} in a week.')
    

#Step3
def throughput_day(par1='8'):
    cap_minute = 24
    cap_hour = cap_minute * 60
    global cap_day
    cap_day = cap_hour * float(par1)
    return cap_day

def throughput_week(par2='7'):
    cap_week = float(par2) * int(cap_day)
    return cap_week

main()
