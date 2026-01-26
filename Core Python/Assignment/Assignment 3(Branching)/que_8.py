# WAP to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

import random
correct_userid = "admin"
correct_password = "1234"

userid = input("Enter UserID: ")
password = input("Enter Password: ")

if userid == correct_userid and password == correct_password:
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    user_input = int(input("Enter the captcha number shown above: "))
    if user_input == captcha:
        print("Login successful! Verification complete.")
    else:
        print("Failed! Captcha did not match.")  
else:
    print("Invalid UserID or Password")

