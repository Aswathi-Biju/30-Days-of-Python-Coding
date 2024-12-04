while True:
    number = int(input("Enter a number: "))
    if number == 0:
        print("Breaking the loop.")
        break
    elif number < 0:  
        print("Skipping this negative number",number)
        continue
    else:
        print("Your number:", number)
