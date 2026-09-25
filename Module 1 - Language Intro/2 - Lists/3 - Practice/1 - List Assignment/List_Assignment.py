# How well do you understand lists, their functions, and how
# to slice them? Let's find out:

# First, create a list with the values
# 5, 10, 15, and 20, in that order:
fives_list = [5, 10, 15, 20]

# Now, store the last value of the list in
# the variable tail:
tail = fives_list[-1]
print(tail)

# Here is another list
new_list = [1, 2, 3, 4, 5]

# Insert a 0 to the front of the list, then
# append a 6 to the end of the list.
# Hint: Should be two lines of code

new_list.insert(0, 0)
new_list.append(6)
print(new_list)

# Here is the another list:
slicing_list = ["Luke", "Leia", "Han", "Vader", "R2D2"]

# Store the first two elements in this new list:
first_two = slicing_list[:2]
print(first_two)

# Store the last three elements in this list:
last_three = slicing_list[-3:]
print(last_three)

# Lastly, copy the whole list into this list:
slicing_copy = slicing_list.copy
print(slicing_copy)
