# Day 5: If-Elif-Else Conditions #5
## *Task*: Use if, elif, and else to handle multiple conditions.

*Description*:
In Python, `if` is used to check a condition, `elif` (short for "else if") is used to check additional conditions, and `else` runs if none of the previous conditions are met. This allows you to handle multiple conditions in a clean way.

*Example*:
```python
# Ask the user to enter their exam score and print their grade based on the score
score = float(input("Enter your exam score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


 #Now write a program that asks the user for the current temperature and prints:

"It's hot!" if the temperature is 30°C or above.
"It's warm!" if the temperature is between 20°C and 29°C.
"It's cool!" if the temperature is between 10°C and 19°C.
"It's cold!" if the temperature is below 10°C.
