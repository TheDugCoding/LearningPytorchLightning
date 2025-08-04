import numpy as np

#the problem with python is that lists are very flexible but inefficient, each element in a list is an
# object, so a list is a list of references to different objects, these objects may also
# be of different types(dynamic typing, in python we don't need to specify the type of a variable).
# Moreover, these objects are not in contiguous blocks.
#numpy offers a solution for this by simplifying how values are stored, an array contains only entries of the same
#type, so numpy is more efficient because it doesn't need to check for type compatibility
# and provides more functionalities compared to python, but it loses flexibility


#compared to python arrays numpy give the user access to more advanced operations
int_array = np.array([1, 4, 2, 5, 3])
print(int_array)

#we can also decide the type of the array
float_array = np.array([1, 2, 3, 4], dtype='float32')
print(float_array)

#also they can be multidimensional
print([range(i, i + 3) for i in [2, 4, 6]])
matrix_int = np.array([range(i, i + 3) for i in [2, 4, 6]])
print(matrix_int)

# Create a length-10 integer array filled with zeros
print(np.zeros(10, dtype=int))

# Create a 3x5 floating-point array filled with 1s
print(np.ones((3, 5), dtype=float))

# Create a 3x5 array filled with 3.14
print(np.full((3, 5), 3.14))

# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
print(np.arange(0, 20, 2))

# Create an array of five values evenly spaced between 0 and 1
print(np.linspace(0, 1, 5))

# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
print(np.random.random((3, 3)))

#if we use random we can set a seed for reproducibility
np.random.seed(0)

#to check an array size we can use these three attributes
# .ndim for the number of dimensions
# .shape for the size of each dimension
# .size for the total size of the array (total number of entries)

#accessing elements is similar to lists
array_accessing = np.ones((10,10))
print(array_accessing[5,5])

#in a multidimensional array you can use slicing like this x[start:stop:step]
#there is also x[5::7] start from 5 but ignore 7

#VERY IMPORTANT, if we put a subarray in a variable and then we modify the subarray the changes will also
#apply to the original array, use .copy() to change elements without affecting the original array

#reshaping, means change the structure of an array, the size of the initial array must be the same of the final array
grid = np.arange(1, 10).reshape((3, 3))
print(grid)

#concatenate np.concatenate, np.vstack, and np.hstack
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(x, y)
print('concatenate', np.concatenate([x, y]))

grid = np.array([[1, 2, 3],
                [4, 5, 6]])

# concatenate along the first axis
print('concatenate along the first axis', np.concatenate([grid, grid]))
# concatenate along the second axis
print('concatenate along the second axis', np.concatenate([grid, grid], axis = 1))

#but for multidimensional stacking is better to use np.vstack (vertical stack) and np.hstack (horizontal stack)

#splitting is implemented by the functions np.split, np.hsplit, and np.vsplit


'''---Ufunc, ---'''

#python is slow with repeated operations, because it needs to check the type of the elements every time because it
#assigns the correct function for the type
# numpy solves this problem with vectorized operations, it skips the type checking because a numpy array
# contains only one type of elements. Vectorized operations are implemented through ufuncs
# depending on the size of the input we have ufuncs(one input) or binary ufuncs(two inputs)
# ufuncs use the same operator as in python

x = np.arange(4)
print("x =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2) # floor division

'''
operators and np variation are roughly the same
+ np.add Addition (e.g., 1 + 1 = 2)
- np.subtract Subtraction (e.g., 3 - 2 = 1)
- np.negative Unary negation (e.g., -2)
* np.multiply Multiplication (e.g., 2 * 3 = 6)
/ np.divide Division (e.g., 3 / 2 = 1.5)
// np.floor_divide Floor division (e.g., 3 // 2 = 1)
** np.power Exponentiation (e.g., 2 ** 3 = 8)
% np.mod Modulus/remainder (e.g., 9 % 4 = 1)
np.log(x)
np.exp(x)
np.power(3, x)
.sum()
.prod()
.mean()
.std()
.min()
.max()


broadcasting allows to perform ufuncs on arrays of different sizes

explanation
https://www.youtube.com/watch?v=oG1t3qlzq14

Rules of Broadcasting
Broadcasting in NumPy follows a strict set of rules to determine the interaction
between the two arrays:
• Rule 1: If the two arrays differ in their number of dimensions, the shape of the
one with fewer dimensions is padded with ones on its leading (left) side.
• Rule 2: If the shape of the two arrays does not match in any dimension, the array
with shape equal to 1 in that dimension is stretched to match the other shape.
• Rule 3: If in any dimension the sizes disagree and neither is equal to 1, an error is
raised.

remember that dimensions with 1 are always compatible,

(2,3) is not compatible with (3, 2)
(2,) is not compatible with (3, 2), because (2,) ->(padding)->(2, 1)

shape that is compatible
x.shape == (1, 2, 3, 5, 1 ,11, 1, 17)
y.shape ==          (1, 7, 1,  1, 17)

after padding

y.shape == (1, 1, 1, 1, 7, 1,  1, 17)

shape results

(1, 2, 3, 5, 7, 11, 1, 17)

another example
2,3,3
3,
after padding
2,3,3
1,3,3

resulting in
2,3,3



'''


#the where function
# Create an array
arr = np.array([10, 15, 20, 25, 30])

# Use np.where() to find indices of elements greater than 20
result = np.where(arr > 20)

print(result)

# Create an array
arr = np.array([10, 15, 20, 25, 30])

# Use np.where() to replace values based on condition
# If the value is greater than 20, return 1, otherwise return 0
result = np.where(arr > 20, 1, 0)

print(result)

# Create two arrays
arr1 = np.array([10, 15, 20, 25, 30])
arr2 = np.array([100, 150, 200, 250, 300])

# Use np.where() to select elements from arr1 where the condition is true, and arr2 otherwise
result = np.where(arr1 > 20, arr1, arr2)

print(result)