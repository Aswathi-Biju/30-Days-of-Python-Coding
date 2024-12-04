num_set1={0,1,2,3,4}
print("Number set: ",num_set1)
num_set1.add(5)
print("After adding an element in number set: ",num_set1)
num_set1.remove(5)
print("After removing an element in number set: ",num_set1)
num_set1.discard(7)
print("After discarding an element, which is not in number set: ",num_set1)
num_set2={5,6,7,8,9}
union_set=num_set1 | num_set2
print("Two sets after union: ",union_set)
intersection_set=num_set1 & num_set2
print("Two sets after intersection: ",intersection_set)
difference_set=num_set1 - num_set2
print("Two sets after difference: ",difference_set)
symmetric_difference_set=num_set1 ^ num_set2
print("Two sets after symmetric difference: ",symmetric_difference_set)
for numbers in num_set1:
    print("Iterating number set one: ",numbers)

