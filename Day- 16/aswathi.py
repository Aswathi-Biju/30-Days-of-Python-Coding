color_list=["Blue","Red","Yellow","Green","White"]
print("Normal list ",color_list)
color_list.append("Black")
print("After appending Black ",color_list)
color_list.insert(1,"Purple")
print("After inserting Purple ",color_list)
color_list.remove("Red")
print("After removing Red ",color_list)
color_list.reverse()
print("After reversing ",color_list)
color_list.sort()
print("After sorting ",color_list)
print("No. of times white color appeared ",color_list.count("White"))
print("Index of Yellow ",color_list.index("Yellow"))