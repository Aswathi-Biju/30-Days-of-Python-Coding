favourite_fruit=input("enter your favourite fruit")

match favourite_fruit:
    case "Apple":
        print("An apple a day keeps the doctor away!")
    case "Banana":
        print("Bananas are a great source of energy.")
    case "Orange":
        print("Oranges are full of Vitamin C.")
    case _:
        print("I don't know that fruit!")
