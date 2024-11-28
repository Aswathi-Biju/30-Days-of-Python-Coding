# **Day 17: Working with Tuples**  
## **Task**: Understand and perform operations with tuples.  

### **Description**:  
A tuple is a collection of items that is ordered and immutable (cannot be modified). Tuples are defined by enclosing elements in parentheses `()`. In this task, you will:  
- Create tuples.  
- Access elements in a tuple.  
- Use tuple operations like concatenation and repetition.  
- Explore tuple-specific functions.  

### **Example**:  
```python
# Step 1: Create a tuple
fruits = ("apple", "banana", "cherry")
print("Original tuple:", fruits)  # Output: ("apple", "banana", "cherry")

# Step 2: Access elements using indexing
print("First fruit:", fruits[0])  # Output: apple
print("Last fruit:", fruits[-1])  # Output: cherry

# Step 3: Slicing a tuple
print("First two fruits:", fruits[:2])  # Output: ("apple", "banana")

# Step 4: Concatenate two tuples
more_fruits = ("orange", "grape")
all_fruits = fruits + more_fruits
print("Combined tuple:", all_fruits)  # Output: ("apple", "banana", "cherry", "orange", "grape")

# Step 5: Repeat a tuple
repeated = fruits * 2
print("Repeated tuple:", repeated)  # Output: ("apple", "banana", "cherry", "apple", "banana", "cherry")

# Step 6: Check for membership
print("Is 'apple' in the tuple?", "apple" in fruits)  # Output: True
print("Is 'kiwi' in the tuple?", "kiwi" in fruits)  # Output: False

# Step 7: Find the length of a tuple
print("Length of the tuple:", len(fruits))  # Output: 3

### Write a program with following tasks:
1. Create a tuple of at least 5 of your favorite colors or animals or items.
2. Perform the following operations:
    Access and print the first and last elements of the tuple using indexing.
    Slice the tuple to extract the first three elements.
    Concatenate your tuple with another tuple of at least 3 elements.
    Repeat your tuple 3 times and print the result.
    Check if a specific item exists in the tuple using the in operator.
    Find the length of the tuple using the len() function.
