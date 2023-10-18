list1 = [] # Empty list
list2 = [67, 90, 12, 88]  #List with integer elements
list3 = ['python', 6732, 45.23, 'jack, 100.2,'] # list with mixed data types
print("List1 = ", list1) # print empty list
print("List2 = ", list2) # prints complete list 2
del list2[2]   #Delete 2nd element in list 2
print("Updated list2", list2)

print("First element of list3 = ", list3[0]) # Prints first element of the list 3
print("Sliced list3 =", list3[1:3]) # prints element starting from 2nd till 3rd
print("Sliced list3 =", list3[2:]) # prints elements starting from 3rd element
print("Repeated list3 = ", list3 * 2)  # prints list 3 two times
print("Concatenated updated list2 & list3", list2 + list3)
