# Day 4: If-Else Conditions #4
## *Task*: Use if-else conditions to make decisions in a program.

*Description*:
In Python, `if` statements are used to check if a condition is true, and `else` is used to define what happens if the condition is false. You can use comparison operators like `==`, `>`, `<`, `>=`, `<=`, and `!=` to compare values.

*Example*:
```python
# Ask the user for a number and check if it is positive, negative, or zero
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
