# Day 6: Case Structure #6
## *Task*: Use a case structure to handle multiple conditions.

*Description*:
The case structure (`match-case` in Python 3.10) allows you to compare a value against multiple cases, similar to switch-case in other programming languages. It provides a clear way to handle multiple specific cases.

*Example*:
```python
# Ask the user to choose a day of the week and print the corresponding message
day = input("Enter a day of the week (e.g., Monday): ")

match day:
    case "Monday":
        print("Start of the work week.")
    case "Tuesday":
        print("Second day of the week.")
    case "Wednesday":
        print("Midweek already!")
    case "Thursday":
        print("Almost there.")
    case "Friday":
        print("Last working day of the week!")
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("Invalid day entered.")

#Now Write a program that asks the user to choose their favorite fruit and prints a message depending on their choice:

Apple: "An apple a day keeps the doctor away!"
Banana: "Bananas are a great source of energy."
Orange: "Oranges are full of Vitamin C."
Any other input: "I don't know that fruit!"
