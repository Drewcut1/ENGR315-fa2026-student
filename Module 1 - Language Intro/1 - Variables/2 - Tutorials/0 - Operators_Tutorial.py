# !! use an import here for math !!
import math as m

# Let's run through some simple operations:

# First, let's go through the steps to find the magnitude
# of two vectors:

vector_one = 16
vector_two = 23

# First, let's square each vector. Use whichever method you like:
one_squared = m.pow(vector_one, 2)
two_squared = m.pow(vector_two, 2)


# Next, let's add the two vectors together:
vector_sum = one_squared + two_squared

# Finally, find the square root of the sum. Use any method:
magnitude = m.sqrt(vector_sum)

# Use a print statement to check your work!
# Answer should be around 28.
print(magnitude)

# Now, try to do that process all in one step!
magnitude_two = m.sqrt((m.pow(vector_one, 2) + m.pow(vector_two, 2)))
print(magnitude_two)
