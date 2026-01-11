# WAP to check if user has entered correct userid and password.

# Predefined correct credentials
correct_userid = "admin"
correct_password = "1234"

# Input from user
userid = input("Enter UserID: ")
password = input("Enter Password: ")

# Check credentials
if userid == correct_userid and password == correct_password:
    print("Login successful")
else:
    print("Invalid UserID or Password")
