size=int(input("enter the size of the multiplication table"))

for i in range(1, size+1):
             for j in range(1, size+1):
                 print(i * j, end="\t")  
             print()