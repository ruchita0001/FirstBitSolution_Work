# WAP to check if entered year is a leap year or not

def ch_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")
        
y = int(input("Enter a year: "))
ch_leap(y)