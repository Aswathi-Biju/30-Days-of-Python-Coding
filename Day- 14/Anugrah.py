while True:
    num = int(input("Enter a number: "))
    if num == 0:
        print("Stop")
        break
    elif num < 0:
        print("Skip",num)
        continue
    else:
        print("Your number: ",num)
    