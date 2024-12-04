number_list=[ ]
for i in range(5):
    number_list.append(int(input(f"Enter number_{i+1}: ")))
print("Number List:",number_list)
print("First Number:",number_list[0],", Last Number:",number_list[-1])
print("The 3 middle elements:",number_list[1:4])
random_list=[100,200]
concatenating_list=number_list+random_list
print("List concatenated:",concatenating_list)
if 50 in concatenating_list:
    print("50 is in the list given")
else:
    print("50 is not in the list")
