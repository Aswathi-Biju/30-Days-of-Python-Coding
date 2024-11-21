limit = int(input("Enter your limit"))
for i in range (1, limit+1):
    for j in range (1, limit+1):
        print(i * j, end="\t")
    print()


