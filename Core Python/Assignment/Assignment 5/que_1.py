userid = input("Enter the UserID : ")
Password = input("Enter the Password : ")

c_userid = "rucha"
c_pass = "12345"

if userid == c_userid and Password == c_pass:
        print("Login Successfully!")
else:
    print("You get 3 chances to enter correct credentials! ")
    for i in range(1, 4):
        if userid == c_userid and Password == c_pass:
            print("Login Successfully!")
        else:    
            userid = input("Enter the UserID : ")
            Password = input("Enter the Password : ")
