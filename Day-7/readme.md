# Day 7: While Loop #7
## *Task*: Use a while loop to repeat actions until a condition is met.

*Description*:
A `while` loop in Python repeats a block of code as long as the condition is `True`. It's great for tasks where you don't know in advance how many times the loop should run.

*Example*:
```python
# Print numbers from 1 to 5 using a while loop
count = 1

while count <= 5:
    print("Number:", count)
    count += 1

#Now write a program that:
Asks the user for a password.
Keeps asking for the password until the correct one is entered.
Print "Access granted" if the correct password is entered, and "Try again" otherwise.
