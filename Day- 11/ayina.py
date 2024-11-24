number=int(input("Enter a number: "))
for num in range (2,number):
    if number%num==0:
        print(number ,"is not Prime number")
        break
else:
    print(number,"is Prime number")