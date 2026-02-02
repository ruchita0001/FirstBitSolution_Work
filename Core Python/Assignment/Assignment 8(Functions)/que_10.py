# WAP to check if entered year is a leap year or not

n = int(input("Enter year: "))

def is_leap_year(n):
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else: 
        return False

if is_leap_year(n):
    print("Leap year")
else:
    print("Not a leap year")
