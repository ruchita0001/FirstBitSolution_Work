#Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1 = int(input("Enter marks of sub1: "))
sub2 = int(input("Enter marks of sub2: "))
sub3 = int(input("Enter marks of sub3: "))
sub4 = int(input("Enter marks of sub4: "))
sub5 = int(input("Enter marks of sub5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

if percentage >= 60:
    print("First Class")
elif percentage >= 50:
    print("Second Class")
elif percentage >= 40:
    print("Third Class")
else:
    print("Fail")
