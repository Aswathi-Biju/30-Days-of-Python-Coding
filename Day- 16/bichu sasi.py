color =["Blue","Red","Yellow","Green","White"]
print("Normal list ",color)
color.append("Black")
print("After appending Black ",color)
color.insert(1,"Purple")
print("After inserting Purple ",color)
color.remove("Red")
print("After removing Red ",color)
color.reverse()
print("After reversing ",color)
color.sort()
print("After sorting ",color)
print("No. of times white color appeared ",color.count("White"))
print("Index of Yellow ",color.index("Yellow"))
