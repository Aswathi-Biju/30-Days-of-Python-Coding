# Day 10: Multiplication Table #10
## *Task*: Use nested loops to create a multiplication table.

*Description*:
A multiplication table is a grid where each cell represents the product of two numbers. Using nested loops, you can generate a table dynamically by iterating through rows and columns.

*Example*:
```python
# Multiplication table from 1 to 5
for i in range(1, 6):  # Outer loop for rows
    for j in range(1, 6):  # Inner loop for columns
        print(i * j, end="\t")  # Print the product with tab spacing
    print()  # Move to the next line after each row

# Write a program that:
Asks the user for the size of the multiplication table (e.g., 5 for a 5x5 table).
Generates the multiplication table using nested loops.
Prints the table neatly with tab (\t) spacing.
