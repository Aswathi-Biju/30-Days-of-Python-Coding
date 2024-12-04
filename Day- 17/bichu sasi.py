colors =("Blue","Purple","White","Black","Grey")
print("My color Tuple: ",colors)
print("First Element: ",colors [0],"Final Element: ",colors [-1])
print("Slicing to get first three elements: ",colors [0:3])
animals =("Ferret","Panda","Fox")
combined =colors + animals
print("Concatenate Tuple: ",combined)
repeat = combined *3
print("Tuple after repeating: ",repeat)
print("Is White in the tuple: ", "White" in combined)
print("Length of combined tuple: ",len(combined),", Length of repeat tuple",len(repeat))
