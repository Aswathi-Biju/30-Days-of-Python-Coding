while True:
    number = int(input("Enter a number: "))
    if number == 0:
        print("Breaking")
        break
    elif number < 0:
        print("Skipping",number)
        continue
    else:
        print("Your number:", number)