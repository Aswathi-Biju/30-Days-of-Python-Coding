n = int(input("Enter the number of turns: "))
a, b = 0, 1
for _ in range(n):     # Note:  _ is a throwaway variable
    print(a, end=" ")
    a, b = b, a + b
