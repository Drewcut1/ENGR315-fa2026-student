"""
In this example we will use the list object including its
constuctor to create new lists and some class methods
"""

# Step 1: declare a list directly (we won't use the constructor)
declared_list = [1, 2, 3, 4]

# Step 2: use the list constructor list() to create a list
constructed_list = list()

# Step 3: the constructed list should be empty. Let's use the built-in
# method extend() to copy of the contents of one list into another
constructed_list.extend(declared_list)

# Step 4: Equality is interesting when it comes to objects. For lists, there contents
# must be exactly the same to be equal. Let's check.

if declared_list == constructed_list:
    print("Both lists are equal!")
else:
    print("Lists are not equal")

# Step 5: Equality is not the same as being the same exact object. There is a difference between
# equality (==) and whether two variables are the exact same object

if declared_list is constructed_list:
    print("Lists are the same object")
else:
    print("Lists are not the same object")

# Step 6: However if we rename a particular variable things change. Each variable simply points to an
# object. The = operator does not make a copy. It simply changes what 'thing' the variable points towards
declared_list = constructed_list

if declared_list is constructed_list:
    print("Lists are the same object")
else:
    print("Lists are not the same object")

    