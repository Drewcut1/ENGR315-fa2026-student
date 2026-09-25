"""
In this example we'll create our own simple class called Point and then access elements of it
"""

from math import sqrt


class Vector:
    """
    A simple 2D vector class
    """
    def __init__(self, _x=0, _y=0):
        """
        Constructor for Vector
        :param _x: X-coordinate for vector. Default value is 0, unless specified
        :param _y: Y-coordinate for vector. Default value is 0, unless specified
        """
        self.x = _x
        self.y = _y

    def magnitude(self):
        return sqrt(self.x * self.x + self.y * self.y)


# Step 1: Create a basic Vector. It will be initialized at (0,0) with the default constructor
zero = Vector()
print("Origin contains ", zero.x, zero.y)

# Step 2: Create a Vector to (1,2). Use the alternate constructor
new_vector = Vector(1, 2)
print("new_vector contains ", new_vector.x, new_vector.y)

# Step 3: Directly change the class by setting the internal fields
new_vector.x = 3
new_vector.y = 4

# Step 4: Use the Vector class method magnitude() to get the length/magnitude of the vector
mag = new_vector.magnitude()
print("Vector magnitude is ", mag)


