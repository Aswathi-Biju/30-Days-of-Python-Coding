# Day 15: Basics of Lists #15
## *Task*: Learn and practice basic operations with lists.

*Description*:
A **list** in Python is a collection of items, which can include numbers, strings, or even other lists. Lists are one of the most versatile data structures in Python. They are:
- **Ordered**: Elements have a defined order.
- **Mutable**: You can change the elements after the list is created.
- **Dynamic**: Lists can grow or shrink in size.

In this task, you’ll learn:
1. How to create a list.
2. Basic list operations like accessing, modifying, and appending elements.
3. Slicing to extract specific parts of a list.
4. Practice these concepts by completing a task.

---
```python
### **1. Creating a List**
A list is created by enclosing elements in square brackets:

# Examples of lists
numbers = [10, 20, 30, 40, 50]
names = ["Alice", "Bob", "Charlie"]
mixed = [5, "hello", 3.14, True]

--

### 2. Accessing Elements in a List 
You can access elements in a list using their **index**. Indexing starts at `0` for the first element and goes to `-1` for the last element.  
# Example of accessing elements
numbers = [10, 20, 30, 40, 50]

# Accessing specific elements
print(numbers[0])  # First element: 10
print(numbers[3])  # Fourth element: 40
print(numbers[-1])  # Last element: 50
print(numbers[-2])  # Second to last element: 40

---

## **3. Basic List Operations**  
You can modify, add, or remove elements in a list using various operations.  

# Examples of basic list operations
numbers = [10, 20, 30, 40, 50]

# Modify an element
numbers[2] = 35
print(numbers)  # Output: [10, 20, 35, 40, 50]

# Add an element to the end of the list
numbers.append(60)
print(numbers)  # Output: [10, 20, 35, 40, 50, 60]

# Remove an element by its value
numbers.remove(20)
print(numbers)  # Output: [10, 35, 40, 50, 60]

---

## **4. Slicing a List**  
You can extract specific parts of a list using slicing.  

# Examples of slicing a list
numbers = [10, 20, 30, 40, 50]

# Slice a portion of the list
print(numbers[1:4])  # Elements from index 1 to 3: [20, 30, 40]

# Slice from the start to a specific index
print(numbers[:3])   # First three elements: [10, 20, 30]

# Slice from a specific index to the end
print(numbers[2:])   # Elements from index 2 onwards: [30, 40, 50]

# Slice with a step
print(numbers[::2])  # Every second element: [10, 30, 50]

# Reverse the list using slicing
print(numbers[::-1]) # Reverse the list: [50, 40, 30, 20, 10]

---

## **5. List Operators**  
Python lists support various operators, including **concatenation**, **repetition**, **equality**, **relational**, and **membership** operators.  


# Examples of list operators
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [1, 2, 3]

# Concatenate two lists
combined = list1 + list2
print(combined)  # Output: [1, 2, 3, 4, 5, 6]

# Repeat a list multiple times
repeated = list1 * 3
print(repeated)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Equality operators
print(list1 == list3)  # Output: True (both lists have the same elements in the same order)
print(list1 == list2)  # Output: False (different elements)

# Relational operators
print(list1 < list2)  # Output: True (compares elements lexicographically)
print(list1 > list2)  # Output: False

# Membership operators
print(2 in list1)  # Output: True (2 is an element of list1)
print(5 in list1)  # Output: False (5 is not in list1)
print(5 not in list1)  # Output: True (5 is not in list1)

### Write a program that:

1. Creates a list of 5 elements entered by the user.
2. Prints the first and last elements.
3. Slices the list to display the middle 3 elements.
4.Concatenates a new list [100, 200] to the original list.
5.Check for the presence of an element[50] in the list using the in operator.




