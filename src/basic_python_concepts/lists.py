#Lists= collection of items in a particular order, lists are dynamic

planes = ['airbus', 'cessna', 'boeing']

print(planes)
print(planes[0])
#print last element
print(planes[-1])

#change element of a list
planes[0] = 'airbus 600'
print(planes)
#add an element at the end of a list
planes.append('F-35')
print(planes)
#inserting an element in any position, all the elements that are after are shifted
planes.insert(1, 'boeing 737')
print(planes)
#you cam remove an element with del
del planes[0]
print(planes)
#if you want to obtain the last element of a list and remove it you can use pop
popped_element = planes.pop()
print(popped_element)
#you can also use pop to remove an element regardless of the position
popped_element = planes.pop(0)
print(planes)
#by using remove you can select the value to remove
planes.remove('cessna')
print(planes)

"""---SORTING---"""
alphabet = ['b', 'd', 'a', 'c']
numbers = [4, 1, 3, 2]

print(alphabet)
#sorting the elements
alphabet.sort()
print(alphabet)
#we can also select the order
alphabet.sort(reverse=True)
print(alphabet)
#if you want to temporarily change the order of a list you can use sorted()
print(numbers)
print(sorted(numbers))
print(numbers)
#length of a list
print(len(numbers))

# take each letter
for letter in alphabet:
    print(f'letter {letter}')

print('these are some letters\n')

for number in range(1, 11):
    print(number)

#you can also use range for lists
numbers_list = list(range(0, 12, 2))
print(numbers_list)

'''list comprehension'''
exponent = [value+2 for value in range(0, 21, 2)]
print(exponent)

#we can also add an if for example newlist = [expression for item in iterable if condition == True]
#the expression is the outcome and it can be whatever we want
# newlist = [x if x != "banana" else "orange" for x in fruits]

#slicing from 1 to 3
print(exponent[1:3])
#slicing from 0 to 3
print(exponent[:3])
#slicing from 2 to the end of the list
print(exponent[2:])
#you can also loop through a slice
for value in exponent[3:]:
    print(value)

'''Tuples'''
#tuples do not change, compared to lists tuples use ()
immutable = ('a', 'b', 'c')
print(immutable)
# for a single element you need to put a comma
immutable_one_element = ('a',)


