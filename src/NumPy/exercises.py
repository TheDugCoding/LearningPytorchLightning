import numpy as np

#create a simple array with 3 float numbers
simple_array = np.array([10, 32, 12.56], dtype=np.float32)
print(simple_array)

#print an array that goes from 10 to 100 with step 10
simple_array_range = np.array(range(10, 101, 10))
print(simple_array_range)
simple_array_arange = np.arange(31)
print('arange\n', simple_array_range)

#try using a list comprehension for an array from 10 to 30, step 5
simple_array_list_comprehension = np.array([x for x in range(10, 31, 5)])
print(simple_array_list_comprehension)

#create an array of zeroes one, two and three dimensions
array_zeroes_one_dimension = np.zeros(3)
print(array_zeroes_one_dimension)
array_zeroes_two_dimensions = np.zeros([4,4])
print(array_zeroes_two_dimensions)
# you can use tuples or lists for the size it doesn't matter
array_zeroes_three_dimensions = np.zeros((5,5,5),dtype=int)
print(array_zeroes_three_dimensions)

#create an array of ones
array_ones_simple = np.ones((6,6), dtype=int)
print(array_ones_simple)

#create an array of numbers equally separated
array_numbers_equally_separated = np.linspace(0, 10, 20)
print(array_numbers_equally_separated)

#for the last array find dimension, size and total number of elements
print(array_numbers_equally_separated.ndim)
print(array_numbers_equally_separated.shape)
print(array_numbers_equally_separated.size)

#selecting and slicing

array_two_dimensions = np.array([range(x, x+11) for x in [10, 20, 30]])
print(array_two_dimensions)
#selecting a single element
print('single element\n', array_two_dimensions[0,0])
#slicing, select first and third row
print('slicing, select first and third row\n', array_two_dimensions[[0,2]])
#select from 5Th column from 2nd row
print('slicing from 2nd row from 5th column\n', array_two_dimensions[1:, 5:])
#all rows except column 3
print('all rows except column 3\n', array_two_dimensions[:, [i for i in range(array_two_dimensions.shape[1]) if i != 2]])


#ufunc and broadcasting

a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])
#checking the numer of dimensions

print('a shape', a.shape)
print('b shape', b.shape)
# by the rules b has fewer dimensions so we add padding to the left
#  (3,) -> (1, 3)
b = np.array([[x] for x in range(10,31,10)]).reshape(1,3)
print('new b', b, b.shape)
#rule 2
print(a + b)