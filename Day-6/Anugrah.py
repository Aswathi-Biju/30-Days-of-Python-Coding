fav_fruit = input("Enter your favourite fruit: ")

match fav_fruit:
    case "Apple":
        print("An apple a day keeps the doctor away!")
    case "Banana":
        print("Bananas are a great source of energy")
    case "Orange":
        print("Oranges are full of Vitamin C")
    case _:
        print("That's an interesting choice!")        
