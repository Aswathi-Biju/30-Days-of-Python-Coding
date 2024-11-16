# Day 14: Break and Continue in Loops #14
## *Task*: Use `break` and `continue` to control loop flow.

*Description*:
In Python, the `break` and `continue` statements are used to control the flow of loops. 
- `break`: Exits the loop completely when a certain condition is met.
- `continue`: Skips the current iteration and moves to the next iteration of the loop.

In this task, you'll practice using both to control the behavior of loops in different situations.

*Example*:
```python
# Using break in a loop
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break  # Exit the loop when i equals 5
    print(i)

# Using continue in a loop
for i in range(1, 10):
    if i == 5:
        print("Skipping i =", i)
        continue  # Skip the current iteration when i equals 5
    print(i)

#  Write a program that:

Asks the user to enter numbers until they enter 0.
If the user enters a negative number, the program should skip that input and ask for another number (use continue).
If the user enters 0, the program should stop asking for numbers (use break).
