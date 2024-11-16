# Day 11: Prime Number Checker #11
## *Task*: Use loops to check if a number is prime.

*Description*:
A prime number is a number greater than 1 that has no divisors other than 1 and itself. To check if a number is prime, you can iterate from 2 to the square root of the number and check for divisibility.

*Example*:
```python
# Check if a number is prime
num = 29  # Example number to check

if num > 1:
    for i in range(2, int(num**0.5) + 1):  # Loop from 2 to sqrt(num)
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# Write a program that:

Asks the user to enter a number.
Checks if the number is prime.
Prints whether the number is prime or not.
