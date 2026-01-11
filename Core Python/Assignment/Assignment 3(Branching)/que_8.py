# WAP to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

#WAP: UserID, Password, and 4-digit captcha verification

import random

# Predefined correct credentials
correct_userid = "admin"
correct_password = "1234"

# Step 1: Input UserID and Password
userid = input("Enter UserID: ")
password = input("Enter Password: ")

# Step 2: Verify credentials
if userid == correct_userid and password == correct_password:
    
    # Step 3: Generate 4-digit random number (captcha)
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    
    # Step 4: Ask user to enter the captcha
    user_input = int(input("Enter the captcha number shown above: "))
    
    # Step 5: Verify captcha
    if user_input == captcha:
        print("Login successful! Verification complete.")
    else:
        print("Failed! Captcha did not match.")
        
else:
    print("Invalid UserID or Password")
