correct_password=input("Enter your password: ")
while True:
    password = input("Enter your password:")
    if password == correct_password:
        print("Access Granted")
        break
    else:
        print("Try Again")
