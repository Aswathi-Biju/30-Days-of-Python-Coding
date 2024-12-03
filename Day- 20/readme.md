# **Day 20: Introduction to Recursion**  
## **Task**: Understand and practice recursion in Python.  

### **Description**:  
Recursion is a technique where a function calls itself to solve smaller instances of a problem until it reaches a base case. It is particularly useful for solving problems that can be divided into smaller, similar subproblems, such as calculating factorials, Fibonacci sequences, or traversing data structures.  

### **Key Components of Recursion**:  
1. **Base Case**: The condition under which the recursion stops.  
2. **Recursive Case**: The function calls itself with a smaller problem to eventually reach the base case.  

### **Example**:  

```python
# Step 1: A recursive function to calculate factorial
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Test the factorial function
print("Factorial of 5:", factorial(5))  # Output: 120

# Step 2: A recursive function for the Fibonacci sequence
def fibonacci(n):
    if n <= 1:  # Base case
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Test the Fibonacci function
print("10th Fibonacci number:", fibonacci(10))  # Output: 55

# Step 3: A simple recursive countdown
def countdown(n):
    if n == 0:  # Base case
        print("Time's up!")
    else:
        print(n)
        countdown(n - 1)  # Recursive case

# Test the countdown function
countdown(5)  # Output: 5, 4, 3, 2, 1, Time's up!

# Now do the following tasks by creating diff file for each tasks under ur name:
1. Write a recursive function called sum_natural that calculates the sum of the first n natural numbers. For example, sum_natural(5) should return 15.
2. Write a recursive function called power(base, exponent) that calculates base raised to the power of exponent using recursion. For example, power(2, 3) should return 8.
3. Write a recursive function called reverse_string that takes a string and returns the reversed version of it. For example, reverse_string("hello") should return "olleh".
4. Write a recursive function to calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
