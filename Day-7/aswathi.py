correct_password=input("Enter your correct password: ")
while True:
    password=input("Enter your password: ")
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Try again")
