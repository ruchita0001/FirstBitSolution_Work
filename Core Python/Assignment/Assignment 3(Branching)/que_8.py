# WAP to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

import random
correct_userid = "admin"
correct_password = "1234"
userid = input("Enter UserID: ")
password = input("Enter Password: ")

if userid == correct_userid and password == correct_password:
    print("Login Successful")
    
    captcha = random.randint(1000, 9999)
    print("Enter this number to continue:", captcha)
    user_captcha = int(input("Enter the number: "))
 
    if user_captcha == captcha:
        print("Verification Successful")
    else:
        print("Verification Failed.")   
else:
    print("Invalid UserID or Password")


