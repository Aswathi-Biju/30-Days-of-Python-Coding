# Day 12: Fibonacci Sequence #12
## *Task*: Use loops to generate the Fibonacci sequence.

*Description*:
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. It typically starts with 0 and 1. This task will help you practice using loops to generate and print a sequence of numbers.

The Fibonacci sequence starts as follows: 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...


*Example*:
```python
# Generate Fibonacci sequence up to a certain number
n = 10  # Number of terms in the Fibonacci sequence
a, b = 0, 1  # First two Fibonacci numbers

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b  # Update a and b for the next term

# Write a program that:

Asks the user for the number of terms to generate in the Fibonacci sequence.
Prints the Fibonacci sequence up to the number of terms entered by the user.
