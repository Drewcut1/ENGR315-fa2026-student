


import numpy


vect1 = [1, 2, 3, 4]
vect2 = [5, 6, 7, 8]
vect3 = [9, 10, 11, 12]
vect4 = [13, 14, 15, 16]
arraything = numpy.array([vect1, vect2, vect3, vect4])
print(arraything)

arraysupercool1 = arraything[1,1]
arraysupercool2 = arraything[:,2]
arraysupercool3 = arraything[2, :]
arraysupercool4 = arraything[:, :]

#print(arraysupercool1)
#print(arraysupercool2)
#print(arraysupercool3)
print(arraysupercool4)
