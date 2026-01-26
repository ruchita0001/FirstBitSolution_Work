# WAP to check if user has entered correct userid and password.

C_userid = "Rucha"
C_password = "1234"

userid = input("Enter UserID:")
password = input("Enter Password:")

if userid == C_userid and password == C_password:
    print("login successful")
else:
    print("Invalid UserID or Password")
