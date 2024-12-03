colors_tuple=("Blue","Purple","White","Black","Grey")
print("My color Tuple: ",colors_tuple)
print("First Element: ",colors_tuple[0],"Final Element: ",colors_tuple[-1])
print("Slicing to get first three elements: ",colors_tuple[0:3])
animals_tuple=("Ferret","Panda","Fox")
combined_tuple=colors_tuple+animals_tuple
print("Concatenate Tuple: ",combined_tuple)
repeat_tuple=combined_tuple*3
print("Tuple after repeating: ",repeat_tuple)
print("Is White in the tuple: ", "White" in combined_tuple)
print("Length of combined tuple: ",len(combined_tuple),", Length of repeat tuple",len(repeat_tuple))
