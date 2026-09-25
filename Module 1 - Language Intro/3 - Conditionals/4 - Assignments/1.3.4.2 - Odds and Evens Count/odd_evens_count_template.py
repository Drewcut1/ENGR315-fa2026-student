# bring in randomness cause we need it in our lives
import random

### Begin Dr. Forsyth Code. Do Not Modify ###

# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return vars


# set the maximum length of the list
max_length = 100

# set the maximum upper bound for the list
upper_bound = 1000

# generate a random lists of integers
nums = generate_random_int_list(max_length, upper_bound)

# create two variables to hold the final answers
#num_evens = 0
#num_odds = 0

list_evens = []
list_odds = []

### YOUR CODE BEGINS HERE ###

length = len(nums)
print(nums)
print(length)

for n in range(0, length, 1):
    if nums[n] % 2 == 0:
        list_evens.append(nums[n])
    else:
        list_odds.append(nums[n])

print(list_evens)
print(list_odds)

num_evens = len(list_evens)
num_odds = len(list_odds)

print(num_evens)
print(num_odds)


