list=[ ]
for i in range(5):
    list.append(int(input(f"Enter number_{i+1}: ")))
print("Number List:",list)
print("First Number:",list[0],", Last Number:",list[-1])
print("Slicing the list to get 3 middle elements:",list[1:4])
random_list=[100,200]
concatenating_list=number_list+random_list
print("List concatenated:",concatenating_list)
print(50 in concatenating_list)
