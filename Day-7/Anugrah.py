correct_password = "Password"
while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Try again")
