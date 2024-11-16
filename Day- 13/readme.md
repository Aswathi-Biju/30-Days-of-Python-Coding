# Day 13: Random Numbers #13
## *Task*: Use the `random` module to generate random numbers.

*Description*:
The `random` module in Python provides functions to generate random numbers. This task will help you practice using `random.randint()` to generate random integers within a specified range, and `random.random()` to generate random floating-point numbers between 0 and 1.

*Example*:
```python
import random

# Generate a random integer between 1 and 100
random_integer = random.randint(1, 100)
print("Random Integer:", random_integer)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random Float:", random_float)

# Write a program that:

Generates 5 random integers between 1 and 50.
Prints each of the random integers.
