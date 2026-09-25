"""
In this example we will import functions from the fibo module that is in the same folder.
We can use those functions here after they've been imported
"""

# Directly import the fib and fib2 methods
from fibo import fib, fib2

# call fib and print the results of Fibonacci sequence up to 5
print('Fibonacci sequence to 5: ')
fib(5)

# call fib2 and return the Fibonacci sequence up to 10
sequence = fib2(10)
print('Fibonacci sequence 10: ')
print(sequence)

