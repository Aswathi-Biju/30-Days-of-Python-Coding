# **Day 18: Working with Sets**  
## **Task**: Explore and perform operations on sets.  

### **Description**:  
A set is a collection of unique, unordered items in Python. Sets are defined by enclosing elements in curly braces `{}` or using the `set()` function. In this task, you will:  
- Create sets.  
- Perform basic set operations such as union, intersection, and difference.  
- Explore set methods like `add()`, `remove()`, and `discard()`.  
- Understand how to check membership and compare sets.  

### **Example**:  
```python
# Step 1: Create a set
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)  # Output: {"apple", "banana", "cherry"}

# Step 2: Add an element to the set
fruits.add("orange")
print("After adding an element:", fruits)  # Output: {"apple", "banana", "cherry", "orange"}

# Step 3: Remove an element
fruits.remove("banana")
print("After removing an element:", fruits)  # Output: {"apple", "cherry", "orange"}

# Step 4: Perform set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union of two sets
print("Union:", set_a | set_b)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection of two sets
print("Intersection:", set_a & set_b)  # Output: {3, 4}

# Difference of two sets
print("Difference (A - B):", set_a - set_b)  # Output: {1, 2}

# Symmetric Difference of two sets
print("Symmetric Difference:", set_a ^ set_b)  # Output: {1, 2, 5, 6}

# Step 5: Check membership
print(3 in set_a)  # Output: True
print(7 in set_a)  # Output: False


# Now try to solve these:
1. Create a set of at least 5 unique items (e.g., numbers, colors, or names).
2. Perform the following operations:
-Add an item to the set using add().
-Remove an item using remove() and discard() (try removing an item that doesn’t exist with discard() to see how it differs from remove()).
-Find the union, intersection, difference, and symmetric difference with another set.
-Check if a specific item exists in your set using the in operator.
-Compare two sets using subset (<=), superset (>=), and disjoint (isdisjoint()) operations.
