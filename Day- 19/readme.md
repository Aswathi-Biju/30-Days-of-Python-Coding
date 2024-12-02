# **Day 19: Introduction to Functions**  
## **Task**: Learn and create basic functions in Python.  

### **Description**:  
Functions are reusable blocks of code that perform a specific task. They allow you to organize your code, avoid repetition, and make it easier to debug and maintain. In this task, you will:  
- Learn how to define and call functions.  
- Understand the use of parameters and return values.  
- Write simple functions to solve basic problems.  

### **Syntax of a Function**:  
```python
def function_name(parameters):
    # Code block
    return value  # Optional
# Step 1: Define a simple function
def greet():
    print("Hello, welcome to Python!")

# Step 2: Call the function
greet()  # Output: Hello, welcome to Python!

# Step 3: Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")  # Output: Hello, Alice!

# Step 4: Function with a return value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Sum:", result)  # Output: Sum: 8

# Now try to do the following tasks:
For this task I have created a seperate folder for everyone in Day- 19 folder, submit ur tasks with naming as (task1.py,task2.py,task3.py,task4.py)

1. Write a function called welcome that prints a welcome message. Call the function.
2. Write a function called multiply that takes two numbers as parameters, multiplies them, and returns the result. Print the returned value.
3. Write a function called is_even that takes a number as a parameter and returns True if the number is even, and False otherwise. Test the function with multiple numbers.
4. Write a function called greet_with_time that takes a name and a time of the day (morning, afternoon, evening) as parameters and prints a greeting like "Good morning, Alice!".
