# **Day 16: List Methods**  
## **Task**: Practice using common list methods.  

### **Description**:  
In this task, you will explore various built-in list methods such as `append()`, `extend()`, `insert()`, `pop()`, `remove()`, `index()`, `count()`, `reverse()`, and `sort()`. These methods allow you to manipulate and analyze lists in Python effectively.  

### **Example**:  
```python
# Step 1: Create a list of numbers
numbers = [10, 20, 30, 40, 50]

# Step 2: Add a new element to the end of the list
numbers.append(60)
print("After append:", numbers)  # Output: [10, 20, 30, 40, 50, 60]

# Step 3: Insert an element at a specific index
numbers.insert(2, 25)
print("After insert:", numbers)  # Output: [10, 20, 25, 30, 40, 50, 60]

# Step 4: Remove a specific element
numbers.remove(40)
print("After remove:", numbers)  # Output: [10, 20, 25, 30, 50, 60]

# Step 5: Pop an element from the end of the list
last_item = numbers.pop()
print("After pop:", numbers)  # Output: [10, 20, 25, 30, 50]
print("Popped item:", last_item)  # Output: 60

# Step 6: Find the index of a specific element
index = numbers.index(30)
print("Index of 30:", index)  # Output: 3

# Step 7: Count occurrences of an element
count = numbers.count(20)
print("Count of 20:", count)  # Output: 1

# Step 8: Reverse the list
numbers.reverse()
print("After reverse:", numbers)  # Output: [50, 30, 25, 20, 10]

# Step 9: Sort the list
numbers.sort()
print("After sort:", numbers)  # Output: [10, 20, 25, 30, 50]


### Write a program with following tasks:
1. Create a list of at least 5 numbers in a list by users input.
2. Use the following list methods:
    Add a new item to the end of the list using append().
    Insert an item at the second position using insert().
    Remove a specific item using remove().
    Reverse the list using reverse().
    Sort the list alphabetically using sort().
3. Print the list after each operation.
4. Count how many times a specific item appears in your list using count().
5. Find the index of a specific item in your list using index().
