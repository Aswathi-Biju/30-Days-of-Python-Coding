# Day 8: Simulating Repeat-Until Loop #8
## *Task*: Use a while loop to simulate a repeat-until loop.

*Description*:
Python doesn't have a built-in `repeat-until` loop like some other languages, but we can simulate this behavior using a `while` loop that always executes the body at least once and stops when a condition is met. This is done by using a `while` loop that keeps repeating until the condition becomes `True`.

*Example*:
```python
# Ask the user for a number and stop when they enter a number greater than 10
number = 0

while True:
    number = int(input("Enter a number: "))
    
    if number > 10:
        print("Number is greater than 10, stopping loop.")
        break  # Exit the loop if number is greater than 10
    else:
        print("Try again.")

# Now write your own program that:
Asks the user for a positive number.
Keeps asking until the user enters a positive number.
Once a positive number is entered, print "Thank you!".
