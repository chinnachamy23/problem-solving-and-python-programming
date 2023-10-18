my_set = {1,3}
print(my_set)

my_set.add(2)  # add an element
print(my_set)

my_set.update([2,3,4])  # add multiple elements
print(my_set)

my_set.update([4,5], {1,6,8})
print(my_set)

# print(my_set[0])  # TypeError: set object does not support indexing

my_set.discard(4) # discard an element in a set
print(my_set)

my_set.remove(6) #remove an element
print(my_set)

my_set.pop() # pop 1st element from a set
print(my_set)

