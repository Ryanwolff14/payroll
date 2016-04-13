def hours():
    hours = int(input('how many hours did you work? '))

    rate = float(input('how much do you make per hour?'))

    if hours<40:
        print("The employee's pay is",(rate*hours))
    if hours>40:
        print("the employee's pay is",((hours-40)*(rate*1.5)+40*rate))
        
def main():
    hours()
 
main()