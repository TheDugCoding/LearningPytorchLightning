from pyparsing import empty

from src.basic_python_concepts.lists import numbers

fruits = ['ananas', 'banana', 'apple']
vegetables = ['carrots', 'milk', 'eggs']
numbers = [1, 2, 3]

for fruit in fruits:
    #if are case sensitive
    if fruit == 'apple':
        print(f'an {fruit} a day make the doctor go away')
    else:
        print(fruit)

for fruit in fruits:
    if fruit != 'banana':
        print('This is not a banana')
    else:
        print('This is a banana')

#use and/or for conditional statements
for vegetable in vegetables:
    for num in numbers:
        for fruit in fruits:
            if fruit == 'apple' or fruit == 'banana' and num == 2 and vegetable == 'carrots':
                print('That is it')

#for checking if a value is in a list you can use not
if 'potato' not in vegetables:
    print('This is not a potato')

#if you need to check multiple statements use if-elif-else, only one statement is executed the other are discarded

topping = 'cheese'

if topping == 'olives':
    print('olives')
elif topping == 'anchovy':
    print('anchovy')
elif topping == 'cheese':
    print('cheese')
else:
    print('other')

#you can also check if a list is empty
empty_list = []

if empty_list:
    print('List is not empty')
else:
    print('List is empty')



