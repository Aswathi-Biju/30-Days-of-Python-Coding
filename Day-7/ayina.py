
true_password=input("enter true password")
while True :
    password = input("enter the password")
    if password==true_password:
        print("Access granted")
        break
    else:
        print("Try again")



