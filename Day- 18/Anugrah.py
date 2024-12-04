unique_set = {"Apple",17,"Black","Dog","Cherry"}
unique_set.add("Orange")
print("After adding an element:",unique_set)
unique_set.remove("Dog")
print("After removing an element:",unique_set)
unique_set.discard(1)
print("After dicarding an element:",unique_set)
set_a = {"Banana",17,"Cherry","Cat","White"}
print("Union:", unique_set | set_a)
print("Intersection:", unique_set & set_a)
print("Difference:", unique_set - set_a)
print("Symmetric difference:", unique_set ^set_a)
print("Is Dog in the set?", "Dog" in unique_set)